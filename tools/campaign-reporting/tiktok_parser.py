import csv
import glob
import os


def find_csv(folder, prefix, since, until):
    pattern = os.path.join(folder, f"{prefix}_{since}_{until}.csv")
    matches = glob.glob(pattern)
    if matches:
        return matches[0]
    fallback = sorted(glob.glob(os.path.join(folder, f"{prefix}_*.csv")))
    return fallback[-1] if fallback else None


def clean_num(val):
    if val is None:
        return 0.0
    val = str(val).replace(",", "").replace("%", "").replace("€", "").replace("$", "").strip()
    if val in ("--", "", "-", "N/A", "n/a"):
        return 0.0
    try:
        return float(val)
    except ValueError:
        return 0.0


def parse_tiktok_csv(path):
    rows = []
    if not path or not os.path.exists(path):
        return rows
    with open(path, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # salta righe totali
            first_val = list(row.values())[0].strip().lower()
            if first_val in ("total", "totale", ""):
                continue
            rows.append(row)
    return rows


def parse_campaigns(path):
    rows = parse_tiktok_csv(path)
    results = []
    for row in rows:
        results.append({
            "campaign": row.get("Campaign name", row.get("Campaign", "?")),
            "status": row.get("Campaign status", row.get("Status", "")),
            "cost": clean_num(row.get("Cost", row.get("Spend", 0))),
            "impressions": clean_num(row.get("Impressions", 0)),
            "clicks": clean_num(row.get("Clicks", 0)),
            "ctr": clean_num(row.get("CTR", 0)),
            "cpc": clean_num(row.get("CPC", row.get("Cost per click", 0))),
            "conversions": clean_num(row.get("Conversions", row.get("Total conversions", 0))),
            "conv_value": clean_num(row.get("Conversion value", row.get("Total conversion value", 0))),
            "roas": clean_num(row.get("ROAS", 0)),
        })
    return results


def parse_adgroups(path):
    rows = parse_tiktok_csv(path)
    results = []
    for row in rows:
        results.append({
            "campaign": row.get("Campaign name", row.get("Campaign", "?")),
            "adgroup": row.get("Ad group name", row.get("Ad Group Name", "?")),
            "status": row.get("Ad group status", row.get("Status", "")),
            "cost": clean_num(row.get("Cost", row.get("Spend", 0))),
            "impressions": clean_num(row.get("Impressions", 0)),
            "clicks": clean_num(row.get("Clicks", 0)),
            "ctr": clean_num(row.get("CTR", 0)),
            "conversions": clean_num(row.get("Conversions", row.get("Total conversions", 0))),
        })
    return results


def parse_ads(path):
    rows = parse_tiktok_csv(path)
    results = []
    for row in rows:
        results.append({
            "campaign": row.get("Campaign name", row.get("Campaign", "?")),
            "adgroup": row.get("Ad group name", row.get("Ad Group Name", "?")),
            "ad": row.get("Ad name", row.get("Ad Name", "?")),
            "cost": clean_num(row.get("Cost", row.get("Spend", 0))),
            "impressions": clean_num(row.get("Impressions", 0)),
            "clicks": clean_num(row.get("Clicks", 0)),
            "ctr": clean_num(row.get("CTR", 0)),
            "video_views": clean_num(row.get("Video views", row.get("Video play actions", 0))),
            "avg_play_time": clean_num(row.get("Average video play time", 0)),
        })
    return results


ALERT_THRESHOLDS = {
    "roas_min": 3.0,
    "ctr_min": 0.5,
}


def check_alerts(campaigns):
    alerts = []
    for c in campaigns:
        if c["cost"] == 0:
            continue
        roas = c["roas"] if c["roas"] > 0 else (c["conv_value"] / c["cost"] if c["cost"] > 0 else 0)
        if c["conv_value"] > 0 and roas < ALERT_THRESHOLDS["roas_min"]:
            alerts.append(f"⚠️  ROAS basso ({roas:.2f}x): {c['campaign']}")
        if c["ctr"] > 0 and c["ctr"] < ALERT_THRESHOLDS["ctr_min"]:
            alerts.append(f"⚠️  CTR basso ({c['ctr']:.2f}%): {c['campaign']}")
    return alerts


def build_report(client_name, since, until, campaigns, adgroups, ads, alerts):
    lines = []
    lines.append(f"# Report TikTok Ads — {client_name.upper()}")
    lines.append(f"**Periodo:** {since} → {until}\n")

    total_cost = sum(c["cost"] for c in campaigns)
    total_conversions = sum(c["conversions"] for c in campaigns)
    total_value = sum(c["conv_value"] for c in campaigns)
    overall_roas = total_value / total_cost if total_cost > 0 else 0

    lines.append("## Riepilogo")
    lines.append(f"- Spesa totale: **€{total_cost:.2f}**")
    lines.append(f"- Conversioni: **{total_conversions:.0f}**")
    lines.append(f"- Valore conversioni: **€{total_value:.2f}**")
    lines.append(f"- ROAS complessivo: **{overall_roas:.2f}x**\n")

    if campaigns:
        lines.append("## Campagne")
        lines.append("| Campagna | Spesa | Conv. | ROAS | CTR | CPC |")
        lines.append("|---|---|---|---|---|---|")
        for c in sorted(campaigns, key=lambda x: x["cost"], reverse=True):
            if c["cost"] == 0:
                continue
            roas = c["roas"] if c["roas"] > 0 else (c["conv_value"] / c["cost"] if c["cost"] > 0 else 0)
            roas_str = f"{roas:.2f}x" if roas > 0 else "—"
            lines.append(f"| {c['campaign']} | €{c['cost']:.2f} | {c['conversions']:.0f} | {roas_str} | {c['ctr']:.2f}% | €{c['cpc']:.2f} |")

    if ads:
        top_ads = sorted([a for a in ads if a["impressions"] > 0], key=lambda x: x["video_views"], reverse=True)[:5]
        if top_ads:
            lines.append("\n## Top annunci per video views")
            lines.append("| Annuncio | Spesa | Video views | CTR | Tempo medio (s) |")
            lines.append("|---|---|---|---|---|")
            for a in top_ads:
                lines.append(f"| {a['ad'][:50]} | €{a['cost']:.2f} | {a['video_views']:.0f} | {a['ctr']:.2f}% | {a['avg_play_time']:.1f}s |")

    lines.append("\n## Alert")
    if alerts:
        for a in alerts:
            lines.append(a)
    else:
        lines.append("✅ Nessuna anomalia rilevata.")

    return "\n".join(lines)
