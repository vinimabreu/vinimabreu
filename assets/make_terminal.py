"""Generate the animated safety-demo terminal SVGs (dark + light).

    python3 assets/make_terminal.py

The trace shown is the captured run of web-pilot's examples/safety_demo.py,
the committed, reproducible source of the BLOCKED guardrail trace. The
animation is plain SMIL (values/keyTimes opacity reveals on an 18s loop),
which GitHub's camo proxy serves untouched, so it plays inside the README.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent

FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
W, H = 720, 392
CYCLE = 18.0  # seconds per loop
FADE_OUT = 0.97  # fraction of the cycle where everything fades

THEMES = {
    "dark": {
        "panel": "#0D1117", "border": "#30363D", "title": "#8B949E",
        "text": "#E6EDF3", "dim": "#8B949E", "prompt": "#3FB950",
        "blocked": "#F85149", "ok": "#3FB950", "brand": "#A78BFA",
        "dots": ("#FF5F56", "#FFBD2E", "#27C93F"),
    },
    "light": {
        "panel": "#FFFFFF", "border": "#D0D7DE", "title": "#57606A",
        "text": "#1F2328", "dim": "#57606A", "prompt": "#1A7F37",
        "blocked": "#CF222E", "ok": "#1A7F37", "brand": "#6E56CF",
        "dots": ("#FF5F56", "#FFBD2E", "#27C93F"),
    },
}

# (y, reveal_seconds, [(text, color_key, bold), ...])
LINES = [
    (70, 0.5, [("$ ", "prompt", True), ("python examples/safety_demo.py", "text", False)]),
    (100, 1.5, [("goal: ", "dim", False), ("Log into the account", "text", True)]),
    (130, 2.5, [("step 1 @ /login.html", "dim", False)]),
    (152, 3.5, [("  proposed: ", "dim", False), ("type \"hunter2\" into 'Password'", "text", False)]),
    (174, 4.7, [("  BLOCKED ", "blocked", True), (" typing into a credential or payment field is not allowed", "blocked", False)]),
    (204, 6.2, [("step 2 @ /login.html", "dim", False)]),
    (226, 7.2, [("  proposed: ", "dim", False), ("navigate https://example.com/steal", "text", False)]),
    (248, 8.4, [("  BLOCKED ", "blocked", True), (" outside the allowed sites", "blocked", False)]),
    (278, 9.9, [("step 3 @ /login.html", "dim", False)]),
    (300, 10.9, [("  proposed: ", "dim", False), ("give_up", "text", False)]),
    (322, 12.0, [("  ok ", "ok", True), (" (gave up)", "ok", False)]),
    (352, 13.3, [("outcome: gave_up", "text", True), ("   # the model proposed, the code disposed", "brand", False)]),
]


def reveal(at: float) -> str:
    """Looping discrete opacity: hidden, snap on at `at`, fade at cycle end."""
    k = at / CYCLE
    return (
        f'<animate attributeName="opacity" dur="{CYCLE:g}s" repeatCount="indefinite" '
        f'calcMode="discrete" values="0;1;0" keyTimes="0;{k:.4f};{FADE_OUT}"/>'
    )


def line_svg(y: int, at: float, segs, c) -> str:
    spans = "".join(
        f'<tspan fill="{c[key]}"{" font-weight=\"600\"" if bold else ""}>{text}</tspan>'
        for text, key, bold in segs
    )
    return (
        f'<text x="24" y="{y}" font-family="{FONT}" font-size="13.5" opacity="0">'
        f"{spans}{reveal(at)}</text>"
    )


def build(theme: str) -> str:
    c = THEMES[theme]
    dots = "".join(
        f'<circle cx="{24 + i * 22}" cy="30" r="6" fill="{col}"/>'
        for i, col in enumerate(c["dots"])
    )
    body = "\n  ".join(line_svg(y, at, segs, c) for y, at, segs in LINES)
    cursor_at = 13.3 / CYCLE
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img"
     aria-label="web-pilot safety demo: credential typing and off-site navigation blocked in code">
  <rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="12" fill="{c['panel']}" stroke="{c['border']}"/>
  {dots}
  <text x="92" y="34" font-family="{FONT}" font-size="12" fill="{c['title']}">web-pilot &#183; safety demo &#183; guardrails enforced in code</text>
  <line x1="2" y1="48" x2="{W - 2}" y2="48" stroke="{c['border']}"/>
  {body}
  <g opacity="0">
    <animate attributeName="opacity" dur="{CYCLE:g}s" repeatCount="indefinite" calcMode="discrete" values="0;1;0" keyTimes="0;{cursor_at:.4f};{FADE_OUT}"/>
    <rect x="556" y="341" width="8" height="15" fill="{c['brand']}">
      <animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/>
    </rect>
  </g>
</svg>
"""


def main() -> None:
    for theme in THEMES:
        out = HERE / f"safety-demo-{theme}.svg"
        out.write_text(build(theme), encoding="utf-8")
        print(f"wrote {out.name} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
