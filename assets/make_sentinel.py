"""Generate the scrape-sentinel terminal SVGs (dark + light).

    python3 assets/make_sentinel.py

A static capture of scrape-sentinel diffing two runs of a product catalog:
one new product, one removed, and one with a price drop and a stock change.
This is the output of the repo's offline demo (examples/demo.py), verbatim.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent

FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
W, H = 720, 392

THEMES = {
    "dark": {
        "panel": "#0D1117", "border": "#30363D", "title": "#8B949E",
        "text": "#E6EDF3", "dim": "#8B949E", "prompt": "#3FB950",
        "added": "#3FB950", "removed": "#F85149", "changed": "#D29922",
        "brand": "#A78BFA", "dots": ("#FF5F56", "#FFBD2E", "#27C93F"),
    },
    "light": {
        "panel": "#FFFFFF", "border": "#D0D7DE", "title": "#57606A",
        "text": "#1F2328", "dim": "#57606A", "prompt": "#1A7F37",
        "added": "#1A7F37", "removed": "#CF222E", "changed": "#9A6700",
        "brand": "#6E56CF", "dots": ("#FF5F56", "#FFBD2E", "#27C93F"),
    },
}

TITLE = "scrape-sentinel · catalog monitor · change detection"

# (y, [(text, color_key, bold), ...])
LINES = [
    (80, [("$ ", "prompt", True), ("scrape-sentinel run --source catalog.json --key sku", "text", False)]),
    (114, [("[scrape-sentinel] catalog: 1 new, 1 changed, 1 removed (2 unchanged)", "brand", True)]),
    (150, [("NEW", "added", True)]),
    (174, [('  + W-104  "Botanical Linen"', "added", False)]),
    (200, [("REMOVED", "removed", True)]),
    (224, [('  - W-099  "Retro Bloom"', "removed", False)]),
    (250, [("CHANGED", "changed", True)]),
    (274, [('  ~ W-101  "Coastal Stripe"', "changed", False)]),
    (296, [("      price: 39.0 -> 35.0", "dim", False)]),
    (318, [("      in_stock: True -> False", "dim", False)]),
    (352, [("# what changed since the last run, down to the field", "brand", False)]),
]


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def line_svg(y: int, segs, c) -> str:
    spans = "".join(
        f'<tspan fill="{c[key]}"{" font-weight=\"600\"" if bold else ""}>{esc(text)}</tspan>'
        for text, key, bold in segs
    )
    return f'<text x="24" y="{y}" font-family="{FONT}" font-size="13.5">{spans}</text>'


def build(theme: str) -> str:
    c = THEMES[theme]
    dots = "".join(
        f'<circle cx="{24 + i * 22}" cy="30" r="6" fill="{col}"/>'
        for i, col in enumerate(c["dots"])
    )
    body = "\n  ".join(line_svg(y, segs, c) for y, segs in LINES)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img"
     aria-label="scrape-sentinel diffing two runs of a product catalog: one new, one removed, one changed with a price drop and stock change">
  <rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="12" fill="{c['panel']}" stroke="{c['border']}"/>
  {dots}
  <text x="92" y="34" font-family="{FONT}" font-size="12" fill="{c['title']}">{esc(TITLE)}</text>
  <line x1="2" y1="48" x2="{W - 2}" y2="48" stroke="{c['border']}"/>
  {body}
</svg>
"""


def main() -> None:
    for theme in THEMES:
        out = HERE / f"sentinel-demo-{theme}.svg"
        out.write_text(build(theme), encoding="utf-8")
        print(f"wrote {out.name} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
