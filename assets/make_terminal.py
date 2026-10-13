"""Generate the animated three-act terminal SVGs (dark + light).

    python3 assets/make_terminal.py

Three scenes on rotation, every one of them a real, reproducible result:

1. betorskip refusing a $84.00 return that Gemma worked out on its own: the
   slip prints "To Win $64.00", so the quote is not on the slip. Verbatim
   output of --explain on the recorded model answer in examples/readings.
2. sequence-gate stopping a send after the invoice was paid, refusing a
   replay, and holding a message at 00:12 in the contact's time zone.
   Captured from examples/demo.py (column spacing trimmed).
3. web-pilot's guardrails blocking a credential field and an off-site jump,
   the captured run of its committed examples/safety_demo.py.

The animation is plain SMIL (discrete opacity reveals on a looping cycle),
which GitHub's camo proxy serves untouched, so it plays inside the README.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent

FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
W, H = 720, 392
ACT = 14.0           # seconds per scene
FADE_GAP = 0.4       # seconds a scene goes dark before the next

THEMES = {
    # Both variants use the mission palette of vinimabreu.dev, so the terminals match the console.
    "dark": {
        "panel": "#05070A", "border": "#26313D", "title": "#6B7683",
        "text": "#D8E1E8", "dim": "#6B7683", "prompt": "#FFB000",
        "blocked": "#FF5C5C", "ok": "#37D67A", "brand": "#FFB000",
        "dots": ("#FF5C5C", "#FFB000", "#37D67A"),
    },
}
THEMES["light"] = THEMES["dark"]

# Each scene: title-bar text + (y, reveal_seconds_into_act, segments) lines.
SCENES = [
    {
        "title": "betorskip · a bet slip read by Gemma 4 · the slip checks the model",
        "lines": [
            (70, 0.5, [("$ ", "prompt", True), ("betorskip examples/slips/us-parlay.txt --rules examples/rules.toml --explain", "text", False)]),
            (104, 1.8, [("BET", "ok", True), (" · stake 4.0% of your bankroll · break-even 23.8%", "text", False)]),
            (126, 2.6, [("bet      PARLAY (2 LEGS) · odds 4.20 · stake $20.00 · to win $64.00", "dim", False)]),
            (148, 3.4, [("note     ignored returns 84: quote is not on the slip", "blocked", False)]),
            (184, 5.0, [("ok", "ok", True), (" stake         20                    \"$20.00\"", "dim", False)]),
            (206, 6.0, [("NO", "blocked", True), (" returns       84                    \"$84.00\"  <- quote is not on the slip", "blocked", False)]),
            (228, 7.0, [("ok", "ok", True), (" to_win        64                    \"$64.00\"", "dim", False)]),
            (250, 8.0, [("ok", "ok", True), (" total_odds    +320                  \"Parlay odds +320\"", "dim", False)]),
            (290, 9.8, [("# Gemma worked out $84.00 on its own · the slip says To Win $64.00", "brand", False)]),
            (316, 11.2, [("# the model proposed a number · the code checked it against the slip", "brand", False)]),
        ],
    },
    {
        "title": "sequence-gate · follow-up sequence · stop before the send",
        "lines": [
            (70, 0.5, [("$ ", "prompt", True), ("python examples/demo.py", "text", False)]),
            (104, 1.6, [("day 0, first email     ", "dim", False), ("SEND", "ok", True), ("  clear  token=tok-1", "dim", False)]),
            (126, 2.4, [("day 3, reminder sms    ", "dim", False), ("SEND", "ok", True), ("  clear  token=tok-2", "dim", False)]),
            (148, 3.4, [("day 4, the invoice is paid", "text", True)]),
            (170, 4.4, [("day 7, final notice    ", "dim", False), ("STOP", "blocked", True), ("  stopping_signal", "blocked", False)]),
            (206, 6.0, [("keyed on (case, step), replay  ", "dim", False), ("SKIP", "blocked", True), ("  already_sent  token=tok-1", "blocked", False)]),
            (242, 7.6, [("contact clock    00:12 in Asia/Kolkata", "dim", False)]),
            (264, 8.6, [("decide           ", "dim", False), ("HOLD", "blocked", True), ("  quiet_hours  retry_after=2026-09-15T02:30:00+00:00", "blocked", False)]),
            (304, 10.4, [("# paid stops the send · a replay is refused · 00:12 local waits", "brand", False)]),
        ],
    },
    {
        "title": "web-pilot · safety demo · guardrails enforced in code",
        "lines": [
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
            (352, 13.0, [("outcome: gave_up", "text", True), ("   # the model proposed, the code disposed", "brand", False)]),
        ],
    },
]

CYCLE = ACT * len(SCENES)


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def window(act_index: int, at: float) -> str:
    """Looping discrete opacity: on at act_start+at, off at act end."""
    on = (act_index * ACT + at) / CYCLE
    off = ((act_index + 1) * ACT - FADE_GAP) / CYCLE
    return (
        f'<animate attributeName="opacity" dur="{CYCLE:g}s" repeatCount="indefinite" '
        f'calcMode="discrete" values="0;1;0" keyTimes="0;{on:.4f};{off:.4f}"/>'
    )


def line_svg(act_index: int, y: int, at: float, segs, c) -> str:
    spans = "".join(
        f'<tspan fill="{c[key]}"{" font-weight=\"600\"" if bold else ""}>{esc(text)}</tspan>'
        for text, key, bold in segs
    )
    return (
        f'<text x="24" y="{y}" font-family="{FONT}" font-size="13.5" opacity="0">'
        f"{spans}{window(act_index, at)}</text>"
    )


def build(theme: str) -> str:
    c = THEMES[theme]
    dots = "".join(
        f'<circle cx="{24 + i * 22}" cy="30" r="6" fill="{col}"/>'
        for i, col in enumerate(c["dots"])
    )
    parts = []
    for i, scene in enumerate(SCENES):
        parts.append(
            f'<text x="92" y="34" font-family="{FONT}" font-size="12" '
            f'fill="{c["title"]}" opacity="0">{scene["title"]}{window(i, 0.0)}</text>'
        )
        parts.extend(line_svg(i, y, at, segs, c) for y, at, segs in scene["lines"])
        last_at = scene["lines"][-1][1]
        parts.append(
            f'<g opacity="0">{window(i, last_at + 0.5)}'
            f'<rect x="24" y="368" width="8" height="15" fill="{c["brand"]}">'
            f'<animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/>'
            f"</rect></g>"
        )
    body = "\n  ".join(parts)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img"
     aria-label="Three captured scenes: betorskip refusing a number the model worked out on its own, sequence-gate stopping a send after payment and refusing a replay, web-pilot guardrails blocking unsafe actions">
  <rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="12" fill="{c['panel']}" stroke="{c['border']}"/>
  {dots}
  <line x1="2" y1="48" x2="{W - 2}" y2="48" stroke="{c['border']}"/>
  {body}
</svg>
"""


def main() -> None:
    for theme in THEMES:
        out = HERE / f"safety-demo-{theme}.svg"
        out.write_text(build(theme), encoding="utf-8")
        print(f"wrote {out.name} ({out.stat().st_size} bytes, {CYCLE:g}s cycle)")


if __name__ == "__main__":
    main()
