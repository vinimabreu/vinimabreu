"""Generate the revenue-loop terminal SVGs (dark + light).

    python3 assets/make_revenue_demo.py

A static capture of revenue-loop's offline demo (python -m examples.loop_demo):
a won deal uploaded once to Google and Meta under one conversion key, the CRM
re-firing the same webhook and sending nothing, and a click that belongs to
another contact quarantined on both platforms. Lines are verbatim from the
demo, in its order, trimmed to these moments; one long Meta line is cut at "...".
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent

FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
W, H = 720, 392

THEMES = {
    # Both variants use the mission palette of vinimabreu.dev, so the terminals match the console.
    "dark": {
        "panel": "#05070A", "border": "#26313D", "title": "#6B7683",
        "text": "#D8E1E8", "dim": "#6B7683", "prompt": "#FFB000",
        "added": "#37D67A", "removed": "#FF5C5C", "changed": "#FFB000",
        "brand": "#FFB000", "dots": ("#FF5C5C", "#FFB000", "#37D67A"),
    },
}
THEMES["light"] = THEMES["dark"]

TITLE = "revenue-loop · CRM won deals to Google and Meta · exactly once"

# (y, [(text, color_key, bold), ...])
LINES = [
    (78, [("$ ", "prompt", True), ("python -m examples.loop_demo", "text", False)]),
    (110, [("1. a deal closes, and the same customer hashes two different ways", "brand", True)]),
    (132, [("conversion key: rl-cdd69e95cbc8127f41c20d755d518d52", "dim", False)]),
    (154, [("  google_ads  uploaded   carrying gclid, email, phone, address", "added", False)]),
    (176, [("  meta        uploaded   carrying fbc, email, phone, given_name, ...", "added", False)]),
    (210, [("2. a lead whose gclid never rendered, and one whose click belongs to somebody else", "brand", True)]),
    (232, [("  opp-7783 google_ads  quarantined  snapshot_belongs_to_another_contact", "removed", False)]),
    (254, [("  opp-7783 meta        quarantined  snapshot_belongs_to_another_contact", "removed", False)]),
    (288, [("3. the CRM re-fires the same won webhook", "brand", True)]),
    (310, [("outcomes:       {'already_uploaded': 2}", "changed", False)]),
    (332, [("requests sent:  0", "changed", False)]),
    (364, [("# uploaded once · the wrong click waits · the re-fire sends nothing", "dim", False)]),
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
     aria-label="revenue-loop: a won deal uploaded once to Google and Meta, a re-fired webhook that sends nothing, and a click from another contact quarantined">
  <rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="12" fill="{c['panel']}" stroke="{c['border']}"/>
  {dots}
  <text x="92" y="34" font-family="{FONT}" font-size="12" fill="{c['title']}">{esc(TITLE)}</text>
  <line x1="2" y1="48" x2="{W - 2}" y2="48" stroke="{c['border']}"/>
  {body}
</svg>
"""


def main() -> None:
    for theme in THEMES:
        out = HERE / f"revenue-demo-{theme}.svg"
        out.write_text(build(theme), encoding="utf-8")
        print(f"wrote {out.name} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
