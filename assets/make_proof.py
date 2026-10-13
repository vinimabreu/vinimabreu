"""Proof tiles: four things a reader can verify, each linked to its evidence.

    python3 assets/make_proof.py

Only what is public and settled goes here: the two paid bounties (receipts on
vinimabreu.dev/proof), the merged upstream fix, and the credited review.
"""

from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
C = {"ground": "#05070A", "hair": "#1C2530", "hair2": "#26313D", "amber": "#FFB000", "green": "#37D67A",
     "text": "#D8E1E8", "muted": "#6B7683"}
W, H = 480, 112

# file stem, label, name, detail; the README links each tile to its evidence
TILES = [
    ("proof-anthropic", "PAID BOUNTY", "Anthropic", "security report, paid"),
    ("proof-mongodb", "PAID BOUNTY", "MongoDB", "security report, resolved and paid"),
    ("proof-crun", "MERGED UPSTREAM", "containers/crun", "PR #2166 · OCI runtime used by Podman"),
    ("proof-arxiv", "CREDITED REVIEWER", "arXiv 2607.18347", "agentic commerce reference architecture"),
]


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def tile(label: str, name: str, detail: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(label.lower())}: {esc(name)}, {esc(detail)}">
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="12" fill="{C['ground']}" stroke="{C['hair2']}"/>
  <path d="M26 28 l5 5 l10 -11" fill="none" stroke="{C['green']}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="52" y="33" font-family="{MONO}" font-size="11" fill="{C['muted']}" letter-spacing="2.5" font-weight="700">{esc(label)}</text>
  <text x="{W - 24}" y="33" text-anchor="end" font-family="{MONO}" font-size="10" fill="{C['muted']}" letter-spacing="1">VERIFY ↗</text>
  <text x="26" y="70" font-family="{SANS}" font-size="24" font-weight="700" fill="{C['amber']}">{esc(name)}</text>
  <text x="26" y="94" font-family="{MONO}" font-size="12" fill="{C['muted']}">{esc(detail)}</text>
</svg>
"""


def main() -> None:
    for stem, label, name, detail in TILES:
        (HERE / f"{stem}.svg").write_text(tile(label, name, detail), encoding="utf-8")
    print(f"wrote {len(TILES)} proof tiles")


if __name__ == "__main__":
    main()
