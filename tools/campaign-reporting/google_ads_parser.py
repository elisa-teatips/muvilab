import csv
import glob
import os
import re


def find_csv(folder, prefix, since, until):
    pattern = os.path.join(folder, f"{prefix}_{since}_{until}.csv")
    matches = glob.glob(pattern)
    if matches:
        return matches[0]
    # fallback: prendi il più recente con quel prefisso
    fallback = sorted(glob.glob(os.path.join(folder, f"{prefix}_*.csv")))
    return fallback[-1] if fallback else None


def parse_google_csv(path):
    """Google Ads CSV ha 2 righe di intestazione da saltare e una riga totali in fondo."""
    rows = []
    if not path or not os.path.exists(path):
        return rows
    with open(path, encoding="utf-8-sig") as f:
        lines = f.readlines()
    # trova la riga header (contiene "Campaign")
    header_idx = None
    for i, line in enumerate(lines):
        if line.startswith('"Campaign"') or line.startswith('Campaign,') or line.startswith('"Campaign,'):
            header_idx = i
            break
        if ',' in line and 'campaign' in line.lower():
            header_idx = i
            break
    if header_idx is None:
        return rows
    reader = csv.DictReader(lines[header_idx:])
    for row in reader:
        campaign = row.get("Campaign", "").strip()
        # salta righe totali e vuote
        if not campaign or campaign.lower() in ("total", "totale", "--"):
            continue
        rows.append(row)
    return rows


def clean_num(val):
    if val is None:
        return 0.0
    val = str(val).replace(",", "").replace("%", "").replace("€", "").strip()
    if val in ("--", "", "-", "< 10"):
        return 0.0
    try:
        return float(val)
    except ValueError:
        return 0.0


def parse_campaigns(path):
    rows = parse_google_csv(path)
    results = []
    for row in rows:
        results.append({
            "campaign": row.get("Campaign", "?"),
            "status": row.get("Campaign status", ""),
            "cost": clean_num(row.get("Cost")),
            "impressions": clean_num(row.get("Impressions")),
            "clicks": clean_num(row.get("Clicks")),
            "ctr": clean_num(row.get("CTR")),
            "avg_cpc": clean_num(row.get("Avg. CPC")),
            "conversions": clean_num(row.get("Conversions")),
            "conv_value": clean_num(row.get("Conv. value")),
            "impr_share": row.get("Search impr. share", "--"),
        })
    return results


def parse_adgroups(path):
    rows = parse_google_csv(path)
    results = []
    for row in rows:
        results.append({
            "campaign": row.get("Campaign", "?"),
            "adgroup": row.get("Ad group", "?"),
            "status": row.get("Ad group status", ""),
            "cost": clean_num(row.get("Cost")),
            "clicks": clean_num(row.get("Clicks")),
            "ctr": clean_num(row.get("CTR")),
            "conversions": clean_num(row.get("Conversions")),
        })
    return results


def parse_assets(path):
    rows = parse_google_csv(path)
    results = []
    for row in rows:
        label = row.get("Performance label", "").strip()
        if not label or label == "--":
            continue
        results.append({
            "campaign": row.get("Campaign", "?"),
            "adgroup": row.get("Ad group", "?"),
            "asset": row.get("Asset", "?"),
            "type": row.get("Asset type", "?"),
            "performance": label,
            "impressions": clean_num(row.get("Impressions")),
            "clicks": clean_num(row.get("Clicks")),
        })
    return results


def parse_keywords(path):
    rows = parse_google_csv(path)
    results = []
    for row in rows:
        results.append({
            "campaign": row.get("Campaign", "?"),
            "keyword": row.get("Keyword", "?"),
            "match_type": row.get("Match type", "?"),
            "cost": clean_num(row.get("Cost")),
            "clicks": clean_num(row.get("Clicks")),
            "ctr": clean_num(row.get("CTR")),
            "avg_cpc": clean_num(row.get("Avg. CPC")),
            "conversions": clean_num(row.get("Conversions")),
            "quality_score": row.get("Quality Score", "--"),
        })
    return results


ALERT_THRESHOLDS_GADS = {
    "roas_min": 3.0,
    "ctr_min": 1.0,
    "quality_score_min": 5,
}


def check_alerts_gads(campaigns, keywords):
    alerts = []
    for c in campaigns:
        if c["cost"] == 0:
            continue
        roas = c["conv_value"] / c["cost"] if c["cost"] > 0 else 0
        if c["conv_value"] > 0 and roas < ALERT_THRESHOLDS_GADS["roas_min"]:
            alerts.append(f"⚠️  ROAS basso ({roas:.2f}x): {c['campaign']}")
        if c["ctr"] > 0 and c["ctr"] < ALERT_THRESHOLDS_GADS["ctr_min"]:
            alerts.append(f"⚠️  CTR basso ({c['ctr']:.2f}%): {c['campaign']}")
    for kw in keywords:
        qs = kw.get("quality_score", "--")
        try:
            if int(qs) < ALERT_THRESHOLDS_GADS["quality_score_min"]:
                alerts.append(f"⚠️  Quality Score basso ({qs}/10): [{kw['match_type']}] {kw['keyword']} — {kw['campaign']}")
        except (ValueError, TypeError):
            pass
    return alerts


def build_gads_report(client_name, since, until, campaigns, adgroups, assets, keywords, alerts):
    lines = []
    lines.append(f"# Report Google Ads — {client_name.upper()}")
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
        lines.append("| Campagna | Spesa | Conv. | ROAS | CTR | CPC medio |")
        lines.append("|---|---|---|---|---|---|")
        for c in sorted(campaigns, key=lambda x: x["cost"], reverse=True):
            if c["cost"] == 0:
                continue
            roas = c["conv_value"] / c["cost"] if c["cost"] > 0 else 0
            roas_str = f"{roas:.2f}x" if c["conv_value"] > 0 else "—"
            lines.append(f"| {c['campaign']} | €{c['cost']:.2f} | {c['conversions']:.0f} | {roas_str} | {c['ctr']:.2f}% | €{c['avg_cpc']:.2f} |")

    if adgroups:
        lines.append("\n## Gruppi di annunci (top per spesa)")
        lines.append("| Gruppo | Campagna | Spesa | CTR | Conv. |")
        lines.append("|---|---|---|---|---|")
        for ag in sorted(adgroups, key=lambda x: x["cost"], reverse=True)[:10]:
            if ag["cost"] == 0:
                continue
            lines.append(f"| {ag['adgroup']} | {ag['campaign']} | €{ag['cost']:.2f} | {ag['ctr']:.2f}% | {ag['conversions']:.0f} |")

    if keywords:
        low_qs = [k for k in keywords if k.get("quality_score", "--") not in ("--", "") and int(k["quality_score"]) < 5]
        top_kw = sorted([k for k in keywords if k["clicks"] > 0], key=lambda x: x["conversions"], reverse=True)[:10]
        if top_kw:
            lines.append("\n## Keyword top per conversioni")
            lines.append("| Keyword | Tipo | Conv. | CTR | CPC | QS |")
            lines.append("|---|---|---|---|---|---|")
            for k in top_kw:
                lines.append(f"| {k['keyword']} | {k['match_type']} | {k['conversions']:.0f} | {k['ctr']:.2f}% | €{k['avg_cpc']:.2f} | {k['quality_score']} |")
        if low_qs:
            lines.append("\n## Keyword con Quality Score basso (<5)")
            lines.append("| Keyword | Tipo | QS | Campagna |")
            lines.append("|---|---|---|---|")
            for k in low_qs:
                lines.append(f"| {k['keyword']} | {k['match_type']} | {k['quality_score']} | {k['campaign']} |")

    if assets:
        best = [a for a in assets if a["performance"] in ("BEST", "GOOD")]
        worst = [a for a in assets if a["performance"] == "LOW"]
        if best:
            lines.append(f"\n## Asset con performance alta ({len(best)} BEST/GOOD)")
            for a in best[:5]:
                lines.append(f"- [{a['type']}] {a['asset'][:60]} — {a['performance']}")
        if worst:
            lines.append(f"\n## Asset con performance bassa ({len(worst)} LOW)")
            for a in worst[:5]:
                lines.append(f"- [{a['type']}] {a['asset'][:60]} — da sostituire")

    lines.append("\n## Alert")
    if alerts:
        for a in alerts:
            lines.append(a)
    else:
        lines.append("✅ Nessuna anomalia rilevata.")

    return "\n".join(lines)
