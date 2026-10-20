#!/usr/bin/env python3
"""Chen conceptual model matching the notation in CSC370-4, slides 9-10."""

from pathlib import Path
import html
import re
import xml.etree.ElementTree as ET
from design import tables

if not __debug__:
    raise SystemExit(
        "Verification requires assertions. Run without -O or PYTHONOPTIMIZE."
    )

root = Path(__file__).resolve().parents[1]
W, H = 2100, 2600
out = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    '<rect width="100%" height="100%" fill="#f7f9fc"/>',
    "<style>text{font-family:Arial,sans-serif;fill:#16304b}.key{text-decoration:underline;font-weight:bold}</style>",
    '<defs><marker id="one" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#43688e"/></marker></defs>',
    '<text x="30" y="38" font-size="28" font-weight="bold">Co-op Application Tracker · Chen conceptual ERD</text>',
    '<text x="30" y="67" font-size="17">Rectangles: entities · ellipses: all descriptive attributes · underlining: chosen identifiers · diamonds: relationships</text>',
    '<text x="30" y="94" font-size="16">Attribute panels and the relationship graph refer to the same named entities. SQL foreign keys are mapped through relationships.</text>',
]
concepts = [(name, t) for name, t in tables.items() if name != "ApplicationResume"]
for i, (name, t) in enumerate(concepts):
    x = 30 + (i % 2) * 1040
    y = 120 + (i // 2) * 400
    attrs = [
        a
        for a, _ in t["cols"]
        if a not in set(re.findall(r"FOREIGN KEY \((\w+)\)", t["body"]))
    ]
    cx = x + 500
    cy = y + 190
    out += [
        f'<g id="concept-{name}">',
        f'<rect x="{x}" y="{y}" width="1000" height="380" rx="12" fill="white" stroke="#d0dce8"/>',
    ]
    for j, a in enumerate(attrs):
        ax = x + (215 if j % 2 == 0 else 785)
        ay = y + 45 + (j // 2) * 53
        out += [
            f'<line x1="{cx-105 if j%2==0 else cx+105}" y1="{cy}" x2="{ax+155 if j%2==0 else ax-155}" y2="{ay}" stroke="#7993b0" stroke-width="1.5"/>'
        ]
    out += [
        f'<rect x="{cx-105}" y="{cy-27}" width="210" height="54" fill="#edf4fb" stroke="#244c73" stroke-width="2"/>',
        f'<text x="{cx}" y="{cy+6}" text-anchor="middle" font-size="20" font-weight="bold">{name}</text>',
    ]
    for j, a in enumerate(attrs):
        ax = x + (215 if j % 2 == 0 else 785)
        ay = y + 45 + (j // 2) * 53
        out += [
            f'<ellipse cx="{ax}" cy="{ay}" rx="155" ry="22" fill="white" stroke="#6586a8"/>',
            f'<text x="{ax}" y="{ay+5}" text-anchor="middle" font-size="16"'
            + (' class="key"' if a in t["keys"][0] else "")
            + f">{html.escape(a)}</text>",
        ]
    out += ["</g>"]
out += [
    '<text x="30" y="1770" font-size="25" font-weight="bold">Relationships and participation</text>',
    '<text x="30" y="1800" font-size="16">(min,max) labels count each entity’s participation; arrows point to an at-most-one related entity. N means many.</text>',
]
nodes = {
    "Student": (200, 1880),
    "ApplicationStatus": (1050, 1880),
    "Employer": (1850, 1880),
    "ResumeVersion": (200, 2150),
    "Application": (1050, 2150),
    "JobPosting": (1850, 2150),
    "Interview": (550, 2500),
    "Offer": (1550, 2500),
}
# Parent, child, relationship, parent participation, child participation.
rels = [
    ("Student", "ResumeVersion", "Owns", "0,N", "1,1"),
    ("Student", "Application", "Submits", "0,N", "1,1"),
    ("Employer", "JobPosting", "Posts", "0,N", "1,1"),
    ("ApplicationStatus", "Application", "Classifies", "0,N", "1,1"),
    ("JobPosting", "Application", "For", "0,N", "1,1"),
    ("Application", "Interview", "Has", "0,N", "1,1"),
    ("Application", "Offer", "Receives", "0,1", "1,1"),
    ("ResumeVersion", "Application", "Selected", "0,N", "0,1"),
]
for parent, child, label, pc, cc in rels:
    ax, ay = nodes[parent]
    bx, by = nodes[child]
    dx = bx - ax
    dy = by - ay
    k = min(115 / abs(dx) if dx else 100, 28 / abs(dy) if dy else 100)
    x1 = ax + dx * k
    y1 = ay + dy * k
    x2 = bx - dx * k
    y2 = by - dy * k
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    out += [
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#43688e" stroke-width="2" marker-start="url(#one)"'
        + (' marker-end="url(#one)"' if pc == "0,1" else "")
        + "/>",
        f'<polygon points="{mx-95},{my} {mx},{my-34} {mx+95},{my} {mx},{my+34}" fill="#eaf1f9" stroke="#43688e" stroke-width="2"/>',
        f'<text x="{mx}" y="{my+5}" text-anchor="middle" font-size="16">{label}</text>',
    ]
    for frac, card in [(0.13, pc), (0.87, cc)]:
        xx = x1 + (x2 - x1) * frac
        yy = y1 + (y2 - y1) * frac - 9
        out += [
            f'<text x="{xx}" y="{yy}" text-anchor="middle" font-size="15" style="paint-order:stroke;stroke:#f7f9fc;stroke-width:5">({card})</text>'
        ]
for name, (cx, cy) in nodes.items():
    out += [
        f'<rect x="{cx-115}" y="{cy-28}" width="230" height="56" fill="white" stroke="#244c73" stroke-width="2"/>',
        f'<text x="{cx}" y="{cy+6}" text-anchor="middle" font-size="19" font-weight="bold">{name}</text>',
    ]
out += ["</svg>"]
(root / "CONCEPTUAL_ERD.svg").write_text("\n".join(out) + "\n")
svg = ET.parse(root / "CONCEPTUAL_ERD.svg").getroot()
ns = {"s": "http://www.w3.org/2000/svg"}
count = 0
for name, t in concepts:
    expected = [
        a
        for a, _ in t["cols"]
        if a not in set(re.findall(r"FOREIGN KEY \((\w+)\)", t["body"]))
    ]
    g = svg.find("s:g[@id='concept-" + name + "']", ns)
    shown = [e.text for e in g.findall("s:text", ns) if e.text in expected]
    assert shown == expected, (name, shown, expected)
    assert len(g.findall("s:ellipse", ns)) == len(expected)
    count += len(expected)
print(
    "PASS Chen notation: 8 entities,",
    count,
    "descriptive attributes/identifiers, 8 relationship diamonds",
)
assert sum(len(re.findall(r"FOREIGN KEY", t["body"])) for t in tables.values()) == 9
assert len(rels) == 8 and count == 50
print(
    "PASS all 9 SQL foreign-key columns represented through the conceptual relationship mapping"
)
