"""The top of the profile as one panel: the header and the live status, nothing else.

    python3 assets/make_console.py && python3 assets/make_hero.py

Built from header.svg and console.svg, each nested at its offset inside one SVG with
its ids prefixed, so the daily refresh of the console carries into the hero. The
house rule paragraph and the receipts live in the README as text and linked tiles.
"""

from __future__ import annotations

import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
W = 1200
GROUND, HAIR = "#05070A", "#1C2530"


def strip_frame(svg: str) -> str:
    """Drop a piece's own outer border, so the pieces share the hero's single frame."""
    return re.sub(r'<rect x="1" y="1" width="\d+" height="\d+" rx="14" fill="#05070A" stroke="#26313D"/>', "", svg, count=1)


def strip_glow(svg: str) -> str:
    """Drop a piece's own corner glow; the hero draws one glow across all pieces instead."""
    return re.sub(r'<rect[^>]*fill="url\(#glow\)"/>', "", svg)


def nest(svg: str, prefix: str, x: float, y: float, w: float) -> tuple[str, float]:
    """Place a whole SVG document at (x, y), scaled to width w; returns the markup and its height."""
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    vw, vh = float(vb.group(1)), float(vb.group(2))
    h = w * vh / vw
    body = svg[svg.index(">", svg.index("<svg")) + 1:svg.rindex("</svg>")]
    body = re.sub(r'id="([^"]+)"', lambda m: f'id="{prefix}-{m.group(1)}"', body)
    body = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{prefix}-{m.group(1)})', body)
    return (f'<svg x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" viewBox="0 0 {vw:g} {vh:g}">{body}</svg>', h)


def main() -> None:
    # the header's own ground and rounded corners would show as a box inside the hero
    header = strip_glow((HERE / "header.svg").read_text(encoding="utf-8"))
    header = re.sub(r'<rect width="\d+" height="\d+" rx="14" fill="#05070A"/>', "", header).replace('rx="14"', 'rx="0"')
    console = strip_glow(strip_frame((HERE / "console.svg").read_text(encoding="utf-8")))
    parts, y = [], 0.0
    piece, h = nest(header, "hd", 0, y, W); parts.append(piece); y += h
    piece, h = nest(console, "co", 0, y, W); parts.append(piece); y += h + 8

    alt = re.search(r'aria-label="([^"]*)"', console).group(1)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {y:.0f}" role="img" '
           f'aria-label="Vinicius Pereira, AI systems that are grounded, tested, and honest. {alt}">\n'
           f'  <rect x="1" y="1" width="{W - 2}" height="{y - 2:.0f}" rx="16" fill="{GROUND}" stroke="#26313D"/>\n  '
           + "\n  ".join(parts) + "\n</svg>\n")
    (HERE / "hero.svg").write_text(svg, encoding="utf-8")
    print(f"wrote hero.svg ({len(svg)} bytes, {y:.0f}px tall)")


if __name__ == "__main__":
    main()
