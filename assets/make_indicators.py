"""Generate the live BCB indicators strip (dark + light), stdlib only.

    python3 assets/make_indicators.py

Fetches the Selic target, 12-month IPCA, and the USD/BRL PTAX rate from the
Central Bank of Brazil's public SGS API (the same API my bcb-data-pipeline
ETL consumes), and renders them into a slim SVG strip. A scheduled GitHub
Action in this repo runs it on weekdays and commits the result only when the
numbers actually changed, so the strip on the profile is always real data
with a commit trail to prove it.

Any fetch or parse failure exits non-zero without touching the SVGs: stale
real numbers beat fresh wrong ones.
"""

import json
import urllib.request
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent

FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
W, H = 720, 64

SERIES = {
    "selic": 432,    # Selic target, % per year
    "ipca": 13522,   # IPCA accumulated over 12 months, %
    "usd": 1,        # USD/BRL PTAX selling rate
}

THEMES = {
    "dark": {"panel": "#0D1117", "border": "#30363D", "dim": "#8B949E",
             "text": "#E6EDF3", "brand": "#A78BFA"},
    "light": {"panel": "#FFFFFF", "border": "#D0D7DE", "dim": "#57606A",
              "text": "#1F2328", "brand": "#6E56CF"},
}


def fetch(series_id: int) -> float:
    url = (f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{series_id}"
           f"/dados/ultimos/1?formato=json")
    with urllib.request.urlopen(url, timeout=30) as resp:
        payload = json.load(resp)
    return float(payload[0]["valor"])


def build(theme: str, selic: float, ipca: float, usd: float) -> str:
    c = THEMES[theme]
    stamp = date.today().isoformat()
    pairs = [("Selic", f"{selic:.2f}%"), ("IPCA 12m", f"{ipca:.2f}%"),
             ("USD/BRL", f"{usd:.2f}")]
    x, items = 56, []
    for label, value in pairs:
        items.append(
            f'<text x="{x}" y="39" font-family="{FONT}" font-size="14">'
            f'<tspan fill="{c["dim"]}">{label} </tspan>'
            f'<tspan fill="{c["text"]}" font-weight="600">{value}</tspan></text>'
        )
        x += 30 + 9 * (len(label) + len(value) + 1)
    body = "\n  ".join(items)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img"
     aria-label="Live Central Bank of Brazil indicators: Selic {selic:.2f} percent, IPCA twelve months {ipca:.2f} percent, USD/BRL {usd:.2f}, refreshed {stamp}">
  <rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="12" fill="{c['panel']}" stroke="{c['border']}"/>
  <circle cx="30" cy="34" r="5" fill="{c['brand']}">
    <animate attributeName="opacity" values="1;0.25;1" dur="2.2s" repeatCount="indefinite"/>
  </circle>
  {body}
  <text x="{W - 24}" y="39" text-anchor="end" font-family="{FONT}" font-size="11" fill="{c['dim']}">BCB SGS &#183; refreshed {stamp}</text>
</svg>
"""


def main() -> None:
    values = {name: fetch(sid) for name, sid in SERIES.items()}
    for theme in THEMES:
        out = HERE / f"indicators-{theme}.svg"
        out.write_text(
            build(theme, values["selic"], values["ipca"], values["usd"]),
            encoding="utf-8",
        )
        print(f"wrote {out.name}: "
              f"Selic {values['selic']:.2f}% IPCA12m {values['ipca']:.2f}% "
              f"USD {values['usd']:.2f}")


if __name__ == "__main__":
    main()
