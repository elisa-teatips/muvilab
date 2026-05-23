#!/usr/bin/env python3

from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd


PRODUCT_REPORT_PATH = Path("/Users/elisa/Downloads/Product report.csv")
ASSET_ASSOCIATION_REPORT_PATH = Path("/Users/elisa/Downloads/Asset association report.csv")
CAMPAIGN_REPORT_PATH = Path("/Users/elisa/Downloads/Campaign report.csv")
OUTPUT_MD_PATH = Path("adv/analisi-google-ads-report-feb-2026.md")


def _to_float(value: object) -> float:
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return float("nan")

    raw = str(value).strip()
    if raw in {"", "--"}:
        return float("nan")

    raw = raw.replace("€", "").replace("EUR", "").strip()
    raw = raw.replace("\u202f", "").replace("\xa0", "")

    # Remove thousands separators like 1,033,113
    raw = re.sub(r"(?<=\d),(?=\d{3}(\D|$))", "", raw)

    # If it's a simple european decimal, normalize, otherwise remove commas.
    if raw.count(",") == 1 and raw.count(".") == 0:
        raw = raw.replace(",", ".")
    else:
        raw = raw.replace(",", "")

    try:
        return float(raw)
    except ValueError:
        return float("nan")


def _to_int(value: object) -> int | None:
    f = _to_float(value)
    if np.isnan(f):
        return None
    return int(round(f))


def _pct_to_float(value: object) -> float:
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return float("nan")

    raw = str(value).strip().replace("%", "")
    if raw in {"", "--"}:
        return float("nan")

    return _to_float(raw) / 100.0


def _fmt_eur(x: float | None) -> str:
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "—"
    # 1,234.56 -> 1.234,56
    return f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def _fmt_int(x: int | float | None) -> str:
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "—"
    return f"{int(x):,}".replace(",", ".")


def _fmt_pct(x: float | None) -> str:
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "—"
    return f"{x * 100:.2f}%".replace(".", ",")


def _fmt_float_it(x: float | None, decimals: int = 2) -> str:
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "—"
    # 1,234.56 -> 1.234,56
    return f"{x:,.{decimals}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def load_product_report(path: Path) -> pd.DataFrame:
    # First two lines are report title + date range
    df = pd.read_csv(path, skiprows=2)

    for col in ["Clicks", "Impr."]:
        df[col] = df[col].map(_to_int)

    for col in ["Avg. CPC", "Cost"]:
        df[col] = df[col].map(_to_float)

    df["CTR"] = df["CTR"].map(_pct_to_float)
    return df


def load_asset_association_report(path: Path) -> pd.DataFrame:
    # Multiline quoted cells in the "Asset" column -> python engine
    df = pd.read_csv(path, skiprows=2, engine="python")

    for col in ["Impr.", "Interactions", "Clicks"]:
        if col in df.columns:
            df[col] = df[col].map(_to_int)

    for col in ["TrueView avg. CPV", "Avg. cost", "Cost", "Conversions"]:
        if col in df.columns:
            df[col] = df[col].map(_to_float)

    if "Interaction rate" in df.columns:
        df["Interaction rate"] = df["Interaction rate"].map(_pct_to_float)

    return df


def load_campaign_report(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, skiprows=2)

    # Normalize numeric columns.
    int_cols = ["Impr.", "Interactions"]
    float_cols = [
        "Budget",
        "TrueView avg. CPV",
        "Avg. cost",
        "Cost",
        "Conv. rate",
        "Conv. value",
        "Conv. value / cost",
        "Conversions",
        "Cost / conv.",
        "Optimization score",
    ]

    for col in int_cols:
        if col in df.columns:
            df[col] = df[col].map(_to_int)

    if "Interaction rate" in df.columns:
        df["Interaction rate"] = df["Interaction rate"].map(_pct_to_float)

    for col in float_cols:
        if col in df.columns:
            if col in {"Conv. rate"}:
                df[col] = df[col].map(_pct_to_float)
            else:
                df[col] = df[col].map(_to_float)

    return df


def main() -> None:
    if not PRODUCT_REPORT_PATH.exists():
        raise SystemExit(f"Missing file: {PRODUCT_REPORT_PATH}")
    if not ASSET_ASSOCIATION_REPORT_PATH.exists():
        raise SystemExit(f"Missing file: {ASSET_ASSOCIATION_REPORT_PATH}")

    p = load_product_report(PRODUCT_REPORT_PATH)
    a = load_asset_association_report(ASSET_ASSOCIATION_REPORT_PATH)
    c: pd.DataFrame | None = None
    if CAMPAIGN_REPORT_PATH.exists():
        c = load_campaign_report(CAMPAIGN_REPORT_PATH)

    p_cost = float(np.nansum(p["Cost"]))
    p_clicks = int(np.nansum(p["Clicks"].astype(float)))
    p_impr = int(np.nansum(p["Impr."].astype(float)))
    p_wctr = (p_clicks / p_impr) if p_impr else float("nan")
    p_avg_cpc = (p_cost / p_clicks) if p_clicks else float("nan")

    p_top = p.sort_values("Cost", ascending=False).head(10).copy()
    p_top["Spend share"] = p_top["Cost"] / p_cost if p_cost else float("nan")

    p_not_eligible_spend = p.loc[p["Status"].astype(str).str.contains("Not eligible", na=False) & (p["Cost"] > 0)].copy()

    a_cost = float(np.nansum(a["Cost"]))
    a_clicks = int(np.nansum(a["Clicks"].astype(float))) if "Clicks" in a.columns else 0
    a_impr = int(np.nansum(a["Impr."].astype(float))) if "Impr." in a.columns else 0
    a_convs = float(np.nansum(a["Conversions"])) if "Conversions" in a.columns else float("nan")

    asset_counts = (
        a.groupby(["Asset type", "Status"], dropna=False)
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
    )

    asset_top_cost = a.sort_values("Cost", ascending=False).head(12).copy()
    asset_bad = a.loc[a["Status"].astype(str).str.contains("Disapproved|Limited", na=False)].copy()

    health_rows = (
        a.loc[a["Asset"].astype(str).str.contains("HEALTH_IN_PERSONALIZED_ADS", na=False)].copy()
        if "Asset" in a.columns
        else a.iloc[0:0].copy()
    )

    lines: list[str] = []
    lines.append("# Neogela — Analisi report Google Ads (Campaign + Product + Asset association)")
    lines.append("Periodo: 1 Feb 2025 – 11 Feb 2026 (come da export)")
    lines.append("")

    lines.append("## Nota importante sui file")
    lines.append("- I CSV in `adv/Neogela-Pu-licità-*` risultano export Meta/Facebook (campi `fb_pixel_purchase`).")
    if c is None:
        lines.append("- Questa analisi usa i 2 report Google Ads: **Product report** e **Asset association report**.")
        lines.append("- Per identificare *tutte* le campagne e valutarle per obiettivo serve anche un export Google Ads ‘Campaigns’.")
    else:
        lines.append("- Questa analisi usa i report Google Ads: **Campaign report**, **Product report** e **Asset association report**.")
        lines.append("- Nota: l’**Asset association report** è un report di *associazione asset* (Account/Campaign). I costi possono risultare non confrontabili 1:1 con i costi campagna (possibili duplicazioni per livello/associazione). Per spesa/ROAS usare il **Campaign report**.")
    lines.append("")

    if c is not None:
        # Filter out total rows.
        c_base = c.loc[~c["Campaign status"].astype(str).str.startswith("Total:", na=False)].copy()
        # Campaign status like Enabled/Paused.
        c_base = c_base.loc[c_base["Campaign status"].astype(str).isin({"Enabled", "Paused"})].copy()

        # Totals row
        totals_row = c.loc[c["Campaign status"].astype(str).eq("Total: Campaigns")]
        if len(totals_row):
            t = totals_row.iloc[0]
            total_cost = float(t.get("Cost"))
            total_conv_value = float(t.get("Conv. value"))
            total_roas = float(t.get("Conv. value / cost"))
            total_conversions = float(t.get("Conversions"))
            total_cpa = float(t.get("Cost / conv."))
        else:
            total_cost = float(np.nansum(c_base.get("Cost", 0)))
            total_conv_value = float(np.nansum(c_base.get("Conv. value", 0)))
            total_roas = (total_conv_value / total_cost) if total_cost else float("nan")
            total_conversions = float(np.nansum(c_base.get("Conversions", 0)))
            total_cpa = (total_cost / total_conversions) if total_conversions else float("nan")

        lines.append("## 0) Campagne — Campaign report")
        lines.append(
            "- Totale account (da Campaign report): "
            f"Spesa {_fmt_eur(total_cost)} | Conv. value {_fmt_eur(total_conv_value)} | "
            f"ROAS {_fmt_float_it(total_roas, 2)} | Conversioni {_fmt_float_it(total_conversions, 2)} | "
            f"CPA {_fmt_eur(total_cpa)}"
        )
        lines.append("")

        c_sorted = c_base.sort_values("Cost", ascending=False).copy()
        if "Cost" in c_sorted.columns and total_cost:
            c_sorted["Spend share"] = c_sorted["Cost"] / total_cost
        else:
            c_sorted["Spend share"] = float("nan")

        lines.append("### Elenco campagne (ordinate per spesa)")
        lines.append("| Campagna | Tipo | Stato | Spesa | Conv. value | ROAS | Conv | CPA | Note |")
        lines.append("|---|---|---|---:|---:|---:|---:|---:|---|")
        for _, r in c_sorted.iterrows():
            roas = r.get("Conv. value / cost")
            roas_s = _fmt_float_it(roas, 2)
            conv = r.get("Conversions")
            conv_s = _fmt_float_it(conv, 2)
            cpa = r.get("Cost / conv.")
            cpa_s = _fmt_eur(cpa)

            status = str(r.get("Status", ""))
            reasons = str(r.get("Status reasons", ""))
            note_parts: list[str] = []
            if "limited by budget" in reasons.lower():
                note_parts.append("budget")
            if "policy" in reasons.lower():
                note_parts.append("policy")
            if "disapproved" in reasons.lower():
                note_parts.append("disapproved")
            if status.startswith("Eligible") and "Limited" in status:
                note_parts.append("eligible-limited")
            note = ", ".join(note_parts) if note_parts else ""

            lines.append(
                "| "
                + " | ".join(
                    [
                        str(r.get("Campaign", "")).replace("|", "/"),
                        str(r.get("Campaign type", "")),
                        str(r.get("Campaign status", "")),
                        _fmt_eur(r.get("Cost")),
                        _fmt_eur(r.get("Conv. value")),
                        roas_s,
                        conv_s,
                        cpa_s,
                        note,
                    ]
                )
                + " |"
            )
        lines.append("")

        # Key insights based on this specific account's campaign mix.
        # Identify top ROAS and worst ROAS among enabled campaigns.
        c_enabled = c_base.loc[c_base["Campaign status"].astype(str).eq("Enabled")].copy()
        if len(c_enabled) and "Conv. value / cost" in c_enabled.columns:
            best = c_enabled.sort_values("Conv. value / cost", ascending=False).iloc[0]
            worst = c_enabled.sort_values("Conv. value / cost", ascending=True).iloc[0]
            lines.append("**Insight campagne**")
            lines.append(
                "- Miglior ROAS (Enabled): "
                + f"**{best.get('Campaign','')}** (ROAS {_fmt_float_it(float(best.get('Conv. value / cost')), 2)}, spesa {_fmt_eur(best.get('Cost'))})."
            )
            lines.append(
                "- Peggior ROAS (Enabled): "
                + f"**{worst.get('Campaign','')}** (ROAS {_fmt_float_it(float(worst.get('Conv. value / cost')), 2)}, spesa {_fmt_eur(worst.get('Cost'))})."
            )
            lines.append("")

        lines.append("**Problemi ricorrenti (da Campaign report)**")
        limited_budget = c_base["Status reasons"].astype(str).str.contains("limited by budget", case=False, na=False).sum()
        limited_policy = c_base["Status reasons"].astype(str).str.contains("policy", case=False, na=False).sum()
        lines.append(f"- Campagne con ‘limited by budget’: {int(limited_budget)}")
        lines.append(f"- Campagne con limitazioni policy negli asset group: {int(limited_policy)}")
        lines.append("")

        lines.append("**Azioni consigliate (per tipo campagna)**")
        lines.append("- Search Brand: aumentare budget finché ROAS/CPA restano efficienti; verificare Impression Share persa per budget/rank; mantenere Brand separato da Non-brand.")
        lines.append("- Search Cold: migliorare struttura per intent (ad group tematici), negative su query poco profittevoli; landing dedicate e RSA con value prop + prova sociale.")
        lines.append("- PMax: risolvere asset/policy (sitelink/landing ‘health sensitive’), segmentare per linea prodotto/bundle con `custom_label`, e valutare esclusioni brand in PMax per evitare cannibalizzazione del Brand Search.")
        lines.append("")

    lines.append("## 1) Shopping / Merchant Center — Product report")
    lines.append(f"- Spesa totale: {_fmt_eur(p_cost)} | Click: {_fmt_int(p_clicks)} | Impression: {_fmt_int(p_impr)}")
    lines.append(f"- CTR pesato: {_fmt_pct(p_wctr)} | CPC medio: {_fmt_eur(p_avg_cpc)}")
    lines.append("")

    lines.append("### Top prodotti per spesa (Top 10)")
    lines.append("| Prodotto | Stato | Click | Impr | CTR | CPC | Spesa | Quota spesa |")
    lines.append("|---|---|---:|---:|---:|---:|---:|---:|")
    for _, r in p_top.iterrows():
        lines.append(
            "| "
            + " | ".join(
                [
                    str(r.get("Title", "")).replace("|", "/"),
                    str(r.get("Status", "")),
                    _fmt_int(r.get("Clicks")),
                    _fmt_int(r.get("Impr.")),
                    _fmt_pct(r.get("CTR")),
                    _fmt_eur(r.get("Avg. CPC")),
                    _fmt_eur(r.get("Cost")),
                    _fmt_pct(r.get("Spend share")),
                ]
            )
            + " |"
        )
    lines.append("")

    if len(p_top) and p_cost:
        top1 = p_top.iloc[0]
        lines.append("**Insight**")
        lines.append(
            f"- Spesa molto concentrata sul prodotto #1: **{top1['Title']}** (quota {_fmt_pct(float(top1['Spend share']))})."
        )
        lines.append("- Senza `Conversions/Conv. value` non possiamo stimare ROAS o CPA dal Product report.")
        lines.append("")

    if len(p_not_eligible_spend):
        lines.append("### Prodotti ‘Not eligible’ con spesa > 0 (storico)")
        lines.append("| Prodotto | Issue | Click | Impr | CPC | Spesa |")
        lines.append("|---|---|---:|---:|---:|---:|")
        for _, r in p_not_eligible_spend.sort_values("Cost", ascending=False).head(10).iterrows():
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(r.get("Title", "")).replace("|", "/"),
                        str(r.get("Issues", ""))[:60].replace("|", "/"),
                        _fmt_int(r.get("Clicks")),
                        _fmt_int(r.get("Impr.")),
                        _fmt_eur(r.get("Avg. CPC")),
                        _fmt_eur(r.get("Cost")),
                    ]
                )
                + " |"
            )
        lines.append("")

    lines.append("**Azioni consigliate (Shopping/PMax)**")
    lines.append("- Feed: sincronizzare disponibilità (Shopify → Merchant Center) ed escludere automaticamente prodotti `out_of_stock`.")
    lines.append("- Struttura: separare best-seller/high-margin in asset group dedicati per evitare cannibalizzazione del budget.")
    lines.append("- Controllo query: affiancare Search Brand (exact/phrase) e Non-brand separata; su PMax usare negative (se disponibili) e segmentazioni per proteggere il brand.")
    lines.append("")

    lines.append("## 2) Asset association report (policy & asset)")
    lines.append(
        f"- Spesa totale asset: {_fmt_eur(a_cost)} | Click: {_fmt_int(a_clicks)} | Impression: {_fmt_int(a_impr)} | Conversioni (da report): {a_convs:.2f}".replace(
            ".", ","
        )
    )
    lines.append("")

    lines.append("### Stati asset (Top)")
    lines.append("| Asset type | Status | Count |")
    lines.append("|---|---|---:|")
    for _, r in asset_counts.head(12).iterrows():
        lines.append(f"| {r['Asset type']} | {r['Status']} | {int(r['count'])} |")
    lines.append("")

    lines.append("### Asset con più spesa (Top)")
    lines.append("| Asset type | Level | Status | Spesa | Click | Conv |")
    lines.append("|---|---|---|---:|---:|---:|")
    for _, r in asset_top_cost.iterrows():
        conv = r.get("Conversions")
        conv_s = "—" if (conv is None or (isinstance(conv, float) and np.isnan(conv))) else f"{float(conv):.2f}".replace(".", ",")
        lines.append(
            "| "
            + " | ".join(
                [
                    str(r.get("Asset type", "")),
                    str(r.get("Level", "")),
                    str(r.get("Status", "")),
                    _fmt_eur(r.get("Cost")),
                    _fmt_int(r.get("Clicks")),
                    conv_s,
                ]
            )
            + " |"
        )
    lines.append("")

    if len(asset_bad):
        lines.append("### Asset ‘Limited’ / ‘Disapproved’ (azioni)")
        lines.append("- Priorità: sostituire asset disapprovati e mitigare limitazioni policy (soprattutto su targeting personalizzato/remarketing).")
        lines.append("| Asset type | Level | Status | Reason | Spesa |")
        lines.append("|---|---|---|---|---:|")
        for _, r in asset_bad.sort_values("Cost", ascending=False).head(12).iterrows():
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(r.get("Asset type", "")),
                        str(r.get("Level", "")),
                        str(r.get("Status", "")),
                        str(r.get("Status reason", "")),
                        _fmt_eur(r.get("Cost")),
                    ]
                )
                + " |"
            )
        lines.append("")

    if len(health_rows):
        lines.append("**Focus: `HEALTH_IN_PERSONALIZED_ADS`**")
        lines.append(f"- Asset impattati: {len(health_rows)}")
        lines.append("- Suggerimento: usare sitelink/asset verso pagine più neutre (brand/prodotto/FAQ), evitando riferimenti diretti a patologie quando si usa remarketing.")
        lines.append("")

    lines.append("## 3) Dati aggiuntivi consigliati (per ottimizzazione avanzata)")
    lines.append("Per andare oltre la lettura a livello campagna (e capire *perché* spendiamo così) conviene esportare anche:")
    lines.append("- Report ‘Search terms’ (o insight PMax) per distinguere Brand vs Non-brand e intercettare query sensibili/mediche che generano CPC alto senza vendite.")
    lines.append("- Segmentazione per device/geo/ora (se vendite sensibili a fascia oraria o aree) e impression share per Search.")
    lines.append("")

    lines.append("## 4) Strategie migliorative (priorità)")
    lines.append("1) **Protezione Brand**: Search Brand (exact/phrase) con RSA + sitelink neutrali; negative su Non-brand/PMax se cannibalizza.")
    lines.append("2) **Struttura PMax per bundle/margine**: asset group separati per Barattolo/Buste/Bundle/Pack e `custom_label` per margine e stock.")
    lines.append("3) **Compliance**: rimuovere riferimenti a patologie nei percorsi asset di campagne con segnali personalizzati; usare pagine prodotto/FAQ generiche.")
    lines.append("4) **Misurazione**: controllare conversion tracking (Purchase, Enhanced Conversions, Consent Mode) e import del valore ordine reale da Shopify.")

    OUTPUT_MD_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {OUTPUT_MD_PATH}")


if __name__ == "__main__":
    main()
