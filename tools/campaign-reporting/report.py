import os
import smtplib
import requests
from google_ads_parser import (
    find_csv as gads_find_csv,
    parse_campaigns as gads_parse_campaigns,
    parse_adgroups as gads_parse_adgroups,
    parse_assets as gads_parse_assets,
    parse_keywords as gads_parse_keywords,
    check_alerts_gads, build_gads_report,
)
from tiktok_parser import (
    find_csv as tiktok_find_csv,
    parse_campaigns as tiktok_parse_campaigns,
    parse_adgroups as tiktok_parse_adgroups,
    parse_ads as tiktok_parse_ads,
    check_alerts as tiktok_check_alerts,
    build_report as tiktok_build_report,
)
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("META_ACCESS_TOKEN")
API_VERSION = "v21.0"
BASE_URL = f"https://graph.facebook.com/{API_VERSION}"

CLIENTS = {
    "neogela": os.getenv("NEOGELA_AD_ACCOUNT_ID"),
}

METRICS = [
    "spend", "impressions", "reach", "clicks", "ctr",
    "cpm", "cpp", "actions", "action_values", "purchase_roas",
    "cost_per_action_type", "frequency",
]

ALERT_THRESHOLDS = {
    "roas_min": 3.0,
    "ctr_min": 0.8,
    "spend_spike_pct": 30,
}


def get_date_range(weeks_back=1):
    today = datetime.today()
    end = today - timedelta(days=today.weekday() + 1)   # domenica scorsa
    start = end - timedelta(days=6)                      # lunedì scorso
    return start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")


def fetch_campaigns(ad_account_id, since, until):
    url = f"{BASE_URL}/{ad_account_id}/campaigns"
    params = {
        "access_token": TOKEN,
        "fields": "id,name,status,objective",
        "effective_status": '["ACTIVE","PAUSED"]',
        "limit": 100,
    }
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json().get("data", [])


def fetch_insights(ad_account_id, since, until):
    url = f"{BASE_URL}/{ad_account_id}/insights"
    params = {
        "access_token": TOKEN,
        "fields": "campaign_name," + ",".join(METRICS),
        "time_range": f'{{"since":"{since}","until":"{until}"}}',
        "level": "campaign",
        "limit": 100,
    }
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json().get("data", [])


def extract_roas(insight):
    roas_list = insight.get("purchase_roas", [])
    if roas_list:
        return float(roas_list[0].get("value", 0))
    return None


def extract_purchases(insight):
    for action in insight.get("actions", []):
        if action.get("action_type") in ("purchase", "offsite_conversion.fb_pixel_purchase"):
            return int(float(action.get("value", 0)))
    return 0


def extract_purchase_value(insight):
    for av in insight.get("action_values", []):
        if av.get("action_type") in ("purchase", "offsite_conversion.fb_pixel_purchase"):
            return float(av.get("value", 0))
    return 0.0


def check_alerts(insights):
    alerts = []
    for i in insights:
        name = i.get("campaign_name", "?")
        spend = float(i.get("spend", 0))
        if spend == 0:
            continue
        roas = extract_roas(i)
        ctr = float(i.get("ctr", 0))
        if roas is not None and roas < ALERT_THRESHOLDS["roas_min"]:
            alerts.append(f"⚠️  ROAS basso ({roas:.2f}x < {ALERT_THRESHOLDS['roas_min']}x): {name}")
        if ctr < ALERT_THRESHOLDS["ctr_min"]:
            alerts.append(f"⚠️  CTR basso ({ctr:.2f}% < {ALERT_THRESHOLDS['ctr_min']}%): {name}")
    return alerts


def build_report(client_name, insights, since, until, alerts):
    lines = []
    lines.append(f"# Report campagne Meta Ads — {client_name.upper()}")
    lines.append(f"**Periodo:** {since} → {until}\n")

    total_spend = sum(float(i.get("spend", 0)) for i in insights)
    total_purchases = sum(extract_purchases(i) for i in insights)
    total_value = sum(extract_purchase_value(i) for i in insights)
    overall_roas = total_value / total_spend if total_spend > 0 else 0

    lines.append("## Riepilogo")
    lines.append(f"- Spesa totale: **€{total_spend:.2f}**")
    lines.append(f"- Acquisti: **{total_purchases}**")
    lines.append(f"- Valore acquisti: **€{total_value:.2f}**")
    lines.append(f"- ROAS complessivo: **{overall_roas:.2f}x**\n")

    lines.append("## Dettaglio campagne")
    lines.append("| Campagna | Spesa | Acquisti | ROAS | CTR | CPM |")
    lines.append("|---|---|---|---|---|---|")

    for i in sorted(insights, key=lambda x: float(x.get("spend", 0)), reverse=True):
        spend = float(i.get("spend", 0))
        if spend == 0:
            continue
        name = i.get("campaign_name", "?")
        purchases = extract_purchases(i)
        roas = extract_roas(i)
        ctr = float(i.get("ctr", 0))
        cpm = float(i.get("cpm", 0))
        roas_str = f"{roas:.2f}x" if roas is not None else "—"
        lines.append(f"| {name} | €{spend:.2f} | {purchases} | {roas_str} | {ctr:.2f}% | €{cpm:.2f} |")

    if alerts:
        lines.append("\n## Alert")
        for a in alerts:
            lines.append(a)
    else:
        lines.append("\n## Alert")
        lines.append("✅ Nessuna anomalia rilevata.")

    return "\n".join(lines)


def save_report(client_name, report_text, since, suffix="-meta-ads"):
    folder = os.path.join(
        os.path.dirname(__file__),
        f"../../clients/muvi-{client_name}/phases/05-reports/{since}/outputs"
    )
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"report{suffix}-{since}.md")
    with open(path, "w") as f:
        f.write(report_text)
    return os.path.abspath(path)


def already_sent(client_name, since, platform):
    flag = os.path.join(
        os.path.dirname(__file__),
        f".sent_{client_name}_{platform}_{since}"
    )
    if os.path.exists(flag):
        return True
    open(flag, "w").close()
    return False


def send_email(subject, body_md, has_alerts, client_name="", since="", platform=""):
    sender = os.getenv("REPORT_EMAIL_FROM")
    password = os.getenv("REPORT_EMAIL_PASSWORD")
    recipient = os.getenv("REPORT_EMAIL_TO")

    if not all([sender, password, recipient]):
        print("Email non configurata, salto invio.")
        return

    if client_name and since and platform and already_sent(client_name, since, platform):
        print(f"Email {platform} già inviata per {since}, salto duplicato.")
        return

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"muvi reporting <{sender}>"
    msg["To"] = recipient

    # versione plain text
    msg.attach(MIMEText(body_md, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
        print(f"Email inviata a {recipient}")
    except Exception as e:
        print(f"Errore invio email: {e}")


def main():
    since, until = get_date_range(weeks_back=1)
    print(f"Periodo analizzato: {since} → {until}\n")

    for client_name, ad_account_id in CLIENTS.items():
        if not ad_account_id:
            print(f"[{client_name}] Ad Account ID mancante, skipping.")
            continue

        print(f"[{client_name}] Scarico insights da Meta API...")
        try:
            insights = fetch_insights(ad_account_id, since, until)
        except requests.HTTPError as e:
            print(f"[{client_name}] Errore API: {e.response.text}")
            continue

        if not insights:
            print(f"[{client_name}] Nessun dato per questo periodo.")
            continue

        alerts = check_alerts(insights)
        report = build_report(client_name, insights, since, until, alerts)

        path = save_report(client_name, report, since)
        print(f"[{client_name}] Report salvato in: {path}")

        if alerts:
            print(f"[{client_name}] {len(alerts)} alert rilevati:")
            for a in alerts:
                print(f"  {a}")
            subject = f"⚠️ Alert campagne {client_name.upper()} — settimana {since}"
        else:
            print(f"[{client_name}] Nessuna anomalia.")
            subject = f"📊 Report campagne {client_name.upper()} — settimana {since}"

        send_email(subject, report, bool(alerts), client_name, since, "meta")
        print()

        # Google Ads (da CSV manuale)
        run_google_ads_report(client_name, since, until)

        # TikTok Ads (da CSV manuale)
        run_tiktok_report(client_name, since, until)


def run_google_ads_report(client_name, since, until):
    folder = os.path.join(
        os.path.dirname(__file__),
        f"imports/{client_name}/google-ads"
    )
    campaigns = gads_parse_campaigns(gads_find_csv(folder, "campaigns", since, until))
    adgroups = gads_parse_adgroups(gads_find_csv(folder, "adgroups", since, until))
    assets = gads_parse_assets(gads_find_csv(folder, "assets", since, until))
    keywords = gads_parse_keywords(gads_find_csv(folder, "keywords", since, until))

    if not campaigns:
        print(f"[{client_name}] Nessun CSV Google Ads trovato per {since}_{until}, skipping.")
        return

    alerts = check_alerts_gads(campaigns, keywords)
    report = build_gads_report(client_name, since, until, campaigns, adgroups, assets, keywords, alerts)

    path = save_report(client_name, report, since, suffix="-google-ads")
    print(f"[{client_name}] Report Google Ads salvato in: {path}")

    subject = (
        f"⚠️ Alert Google Ads {client_name.upper()} — settimana {since}"
        if alerts else
        f"📊 Report Google Ads {client_name.upper()} — settimana {since}"
    )
    send_email(subject, report, bool(alerts), client_name, since, "google-ads")


def run_tiktok_report(client_name, since, until):
    folder = os.path.join(
        os.path.dirname(__file__),
        f"imports/{client_name}/tiktok-ads"
    )
    campaigns = tiktok_parse_campaigns(tiktok_find_csv(folder, "campaigns", since, until))
    adgroups = tiktok_parse_adgroups(tiktok_find_csv(folder, "adgroups", since, until))
    ads = tiktok_parse_ads(tiktok_find_csv(folder, "ads", since, until))

    if not campaigns:
        print(f"[{client_name}] Nessun CSV TikTok Ads trovato per {since}_{until}, skipping.")
        return

    alerts = tiktok_check_alerts(campaigns)
    report = tiktok_build_report(client_name, since, until, campaigns, adgroups, ads, alerts)

    path = save_report(client_name, report, since, suffix="-tiktok-ads")
    print(f"[{client_name}] Report TikTok Ads salvato in: {path}")

    subject = (
        f"⚠️ Alert TikTok Ads {client_name.upper()} — settimana {since}"
        if alerts else
        f"📊 Report TikTok Ads {client_name.upper()} — settimana {since}"
    )
    send_email(subject, report, bool(alerts), client_name, since, "tiktok-ads")


if __name__ == "__main__":
    main()
