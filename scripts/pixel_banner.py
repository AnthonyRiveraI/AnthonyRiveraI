"""Generates the pixel-art SVG assets for the README."""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
random.seed(7)

# ---------- 5x7 pixel font ----------
FONT = {
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "C": ["01110", "10001", "10000", "10000", "10000", "10001", "01110"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "G": ["01110", "10001", "10000", "10111", "10001", "10001", "01111"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "V": ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    "W": ["10001", "10001", "10001", "10101", "10101", "10101", "01010"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "X": ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    " ": ["00000"] * 7,
    "*": ["00000", "00000", "00100", "01110", "00100", "00000", "00000"],
    ">": ["10000", "01000", "00100", "00010", "00100", "01000", "10000"],
    "+": ["00000", "00100", "00100", "11111", "00100", "00100", "00000"],
}


def text_rects(text, x, y, s, color):
    out = []
    cx = x
    for ch in text:
        glyph = FONT[ch]
        for r, row in enumerate(glyph):
            c = 0
            while c < 5:
                if row[c] == "1":
                    start = c
                    while c < 5 and row[c] == "1":
                        c += 1
                    out.append(f'<rect x="{cx + start*s}" y="{y + r*s}" width="{(c-start)*s}" height="{s}" fill="{color}"/>')
                else:
                    c += 1
        cx += 6 * s
    return "".join(out)


def text_width(text, s):
    return len(text) * 6 * s - s


def sprite(rows, palette, x0, y0, s):
    out = []
    for r, row in enumerate(rows):
        c = 0
        while c < len(row):
            ch = row[c]
            if ch in palette:
                start = c
                while c < len(row) and row[c] == ch:
                    c += 1
                out.append(f'<rect x="{x0 + start*s}" y="{y0 + r*s}" width="{(c-start)*s}" height="{s}" fill="{palette[ch]}"/>')
            else:
                c += 1
    return "".join(out)


# ---------- palette ----------
SKY = ["#0b1026", "#111a3a", "#18244d", "#213063"]
SEA = ["#0d3354", "#0f4470", "#14588c"]
FOAM = "#9fd3f0"
GOLD = "#f2c94c"
RED = "#d64545"
CREAM = "#f4ecd8"

W, H, P = 960, 320, 8  # canvas + base pixel size

# ---------- ship sprite (faces right) ----------
SHIP = [
    "..............m.kkkkkkkkkkk.....",
    "..............m.kkkkyyykkkk.....",
    "..............m.kkkyyyyykkk.....",
    "..............m.kkyrrrrrykk.....",
    "..............m.kyyyyyyyyyk.....",
    "..............m.kkkwwwwwkkk.....",
    "..............m.kkwkwwwkwkk.....",
    "..............m.kkwwwkwwwkk.....",
    "..............m.kwkkwwwkkwk.....",
    "..............m.wkkkkkkkkkw.....",
    "......mmmmmmmmmmmmmmmmm.........",
    "......ssssssssssssssssS.........",
    ".....sssssssssssssssssS.........",
    ".....ssssssssrrrssssssSS........",
    "....sssssssssrrrsssssssS........",
    "....ssssssssssssssssssssS.......",
    "....ssssssssssssssssssssS.......",
    ".....sssssssssssssssssSS........",
    ".....sssssssssssssssssS.........",
    "......ssssssssssssssssS.........",
    "......mmmmmmmmmmmmmmmmm.........",
    "hhhh..........m...............m.",
    "hhhhh.........m..............m..",
    "ggggggggggggggggggggggggggggg...",
    "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh..",
    ".hhhhohhhhhohhhhhohhhhhohhhhh...",
    "..HHHHHHHHHHHHHHHHHHHHHHHHHHH...",
    "...HHHHHHHHHHHHHHHHHHHHHHHHH....",
    "....HHHHHHHHHHHHHHHHHHHHHHH.....",
]
# ship's doctor: a tiny reindeer in a pink top hat (Chopper tribute)
CHOPPER = [
    "a..a........a..a",
    ".aa..pppppp..aa.",
    "..a..pwppwp..a..",
    "..aa.ppwwpp.aa..",
    "....apwppwpa....",
    "..pppppppppppp..",
    "...tttttttttt...",
    "...ttkttttktt...",
    "...ttttbbtttt...",
    "....tttttttt....",
    "...ffffffffff...",
    "..ffffffffffff..",
    "..hffffffffffh..",
    "....mmmmmmmm....",
    "....mmm..mmm....",
    "....fff..fff....",
    "....hhh..hhh....",
]
CHOPPER_PAL = {
    "a": "#a0703c", "p": "#f48fb1", "w": "#ffffff", "t": "#f0c8a0", "k": "#14141c",
    "b": "#4f8df5", "f": "#8a5a32", "h": "#f4ecd8", "m": "#b0413e",
}

SHIP_PAL = {
    "m": "#6b3f1f", "k": "#14141c", "y": GOLD, "r": RED, "w": CREAM,
    "s": CREAM, "S": "#cfc4ab", "h": "#8a5a2b", "H": "#5e3a1a",
    "g": "#d9a441", "o": "#2a1a0c",
}
# second flag frame: tip of the flag drops one pixel (waving)
FLAG2_TIP = [
    "kkkkkkkkk..",
    "kkkkyyykkkk",
    "kkkyyyyykkk",
    "kkyrrrrrykk",
    "kyyyyyyyyyk",
    "kkkwwwwwkkk",
    "kkwkwwwkwkk",
    "kkwwwkwwwkk",
    "kwkkwwwkkwk",
    "wkkkkkkkkkw",
    ".........kk",
]


def banner():
    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" shape-rendering="crispEdges">')
    parts.append('<title>Anthony Rivera - AI Engineer</title>')
    # sky bands
    band_h = [64, 64, 64, 56]
    y = 0
    for color, h in zip(SKY, band_h):
        parts.append(f'<rect x="0" y="{y}" width="{W}" height="{h}" fill="{color}"/>')
        y += h
    # dither between bands
    y = 0
    for i, h in enumerate(band_h[:-1]):
        y += h
        for x in range(0, W, P * 2):
            parts.append(f'<rect x="{x + (P if (x // (P*2)) % 2 else 0)}" y="{y - P}" width="{P}" height="{P}" fill="{SKY[i+1]}"/>')
    # stars
    for i in range(46):
        sx = random.randrange(0, W // 4) * 4
        sy = random.randrange(0, 200 // 4) * 4
        if 32 < sx < 600 and 60 < sy < 210:
            continue  # keep the text area clean
        dur = random.choice([2.4, 3.2, 4.0, 5.2])
        begin = round(random.uniform(0, 4), 2)
        big = random.random() < 0.18
        if big:
            g = (f'<rect x="{sx}" y="{sy-4}" width="4" height="12" fill="#fff6d5"/>'
                 f'<rect x="{sx-4}" y="{sy}" width="12" height="4" fill="#fff6d5"/>')
        else:
            g = f'<rect x="{sx}" y="{sy}" width="4" height="4" fill="#c9d6ff"/>'
        parts.append(f'<g>{g}<animate attributeName="opacity" values="1;0.2;1" dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/></g>')
    # moon (pixel circle) with crescent shadow
    mx, my, mr = 640, 44, 4
    for r in range(-mr, mr + 1):
        for c in range(-mr, mr + 1):
            if r * r + c * c <= mr * mr + 2:
                col = "#fff1c1"
                if (r, c) in {(-2, -1), (1, 2), (2, -2), (-1, 2)}:
                    col = "#ffe48a"
                parts.append(f'<rect x="{mx + c*P}" y="{my + r*P}" width="{P}" height="{P}" fill="{col}"/>')
    # seagull (2-frame flap) drifting across
    gull_a = ["w...w", ".w.w.", "..w.."]
    gull_b = [".....", "wwwww", "..w.."]
    gp = {"w": "#e8eefc"}
    parts.append('<g><animateTransform attributeName="transform" type="translate" values="-60 0;1000 -20" dur="22s" repeatCount="indefinite"/>')
    parts.append(f'<g>{sprite(gull_a, gp, 0, 28, 4)}<animate attributeName="opacity" values="1;0" dur="0.6s" calcMode="discrete" repeatCount="indefinite"/></g>')
    parts.append(f'<g opacity="0">{sprite(gull_b, gp, 0, 28, 4)}<animate attributeName="opacity" values="0;1" dur="0.6s" calcMode="discrete" repeatCount="indefinite"/></g>')
    parts.append('</g>')

    # ---------- text ----------
    tx, ty, ts = 48, 84, 6
    title = "ANTHONY RIVERA"
    parts.append(text_rects(title, tx + ts, ty + ts, ts, "#1a0f05"))
    parts.append(text_rects(title, tx, ty, ts, GOLD))
    sub = "AI ENGINEER"
    sy2, ss = ty + 7 * ts + 22, 5
    parts.append(text_rects(sub, tx + 4, sy2 + 4, ss, "#0a0f22"))
    parts.append(text_rects(sub, tx, sy2, ss, CREAM))
    # typed tagline with clip-path reveal + moving cursor
    tags = "> AGENTS + RAG + VOICE + MCP"
    s3 = 3
    ty3 = sy2 + 7 * ss + 24
    n = len(tags)
    widths = [i * 6 * s3 for i in range(n + 1)]
    frames = widths + [widths[-1]] * 14 + [0] * 3
    keyt = ";".join(f"{i/(len(frames)-1):.4f}" for i in range(len(frames)))
    wvals = ";".join(str(v) for v in frames)
    xvals = ";".join(str(tx + v) for v in frames)
    dur = len(frames) * 0.12
    parts.append(f'<defs><clipPath id="type"><rect x="{tx}" y="{ty3-4}" width="0" height="{7*s3+8}">'
                 f'<animate attributeName="width" values="{wvals}" keyTimes="{keyt}" calcMode="discrete" dur="{dur:.2f}s" repeatCount="indefinite"/>'
                 f'</rect></clipPath></defs>')
    parts.append(f'<g clip-path="url(#type)">{text_rects(tags, tx, ty3, s3, FOAM)}</g>')
    parts.append(f'<rect x="{tx}" y="{ty3}" width="{5*s3}" height="{7*s3}" fill="{GOLD}">'
                 f'<animate attributeName="x" values="{xvals}" keyTimes="{keyt}" calcMode="discrete" dur="{dur:.2f}s" repeatCount="indefinite"/>'
                 f'<animate attributeName="opacity" values="1;0" dur="0.8s" calcMode="discrete" repeatCount="indefinite"/></rect>')

    # ---------- sea ----------
    sea_y = 248
    parts.append(f'<rect x="0" y="{sea_y}" width="{W}" height="{H-sea_y}" fill="{SEA[0]}"/>')
    parts.append(f'<rect x="0" y="{sea_y+24}" width="{W}" height="{H-sea_y-24}" fill="{SEA[1]}"/>')
    parts.append(f'<rect x="0" y="{sea_y+48}" width="{W}" height="{H-sea_y-48}" fill="{SEA[2]}"/>')
    # moon reflection
    for i, w in enumerate([5, 3, 4, 2]):
        parts.append(f'<rect x="{mx - (w//2)*P}" y="{sea_y + 8 + i*14}" width="{w*P}" height="4" fill="#ffe48a" opacity="0.55">'
                     f'<animate attributeName="opacity" values="0.55;0.2;0.55" dur="{2+i*0.5}s" repeatCount="indefinite"/></rect>')
    # ---------- ship ----------
    sxp, syp, s = 700, 82, 6
    ship_body = [row[:16] + row[16:27].replace("k", ".").replace("y", ".").replace("r", ".").replace("w", ".") + row[27:] if i < 10 else row for i, row in enumerate(SHIP)]
    flag_a = [row[16:27] for row in SHIP[:10]]
    parts.append('<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -6;0 -6;0 0;0 0" keyTimes="0;0.25;0.5;0.75;1" calcMode="discrete" dur="2.4s" repeatCount="indefinite"/>')
    parts.append(sprite(ship_body, SHIP_PAL, sxp, syp, s))
    parts.append(f'<g>{sprite(flag_a, SHIP_PAL, sxp + 16*s, syp, s)}<animate attributeName="opacity" values="1;0" dur="1.2s" calcMode="discrete" repeatCount="indefinite"/></g>')
    parts.append(f'<g opacity="0">{sprite(FLAG2_TIP, SHIP_PAL, sxp + 16*s, syp, s)}<animate attributeName="opacity" values="0;1" dur="1.2s" calcMode="discrete" repeatCount="indefinite"/></g>')
    # Chopper standing on the bow, hopping every few seconds
    cy = syp + 23 * s - len(CHOPPER) * 3
    parts.append(f'<g>{sprite(CHOPPER, CHOPPER_PAL, sxp + 24*s - 4, cy, 3)}'
                 '<animateTransform attributeName="transform" type="translate" values="0 0;0 -9;0 -3;0 0" '
                 'keyTimes="0;0.06;0.12;0.18" calcMode="discrete" dur="4.8s" repeatCount="indefinite"/></g>')
    parts.append('</g>')

    # wave layers: crest pattern repeated, scrolled left forever
    def wave_layer(y, period, color, dur, crest):
        rects = []
        for x0 in range(-period, W + period, period):
            for (dx, dy, w) in crest:
                rects.append(f'<rect x="{x0+dx}" y="{y+dy}" width="{w}" height="4" fill="{color}"/>')
        return (f'<g><animateTransform attributeName="transform" type="translate" values="0 0;{-period} 0" '
                f'dur="{dur}s" repeatCount="indefinite"/>{"".join(rects)}</g>')
    parts.append(wave_layer(sea_y - 4, 64, FOAM, 3, [(0, 4, 16), (16, 0, 16), (32, 4, 8)]))
    parts.append(wave_layer(sea_y + 18, 96, "#5fa8d3", 5, [(8, 4, 24), (32, 0, 16)]))
    parts.append(wave_layer(sea_y + 42, 128, "#3b86b8", 8, [(16, 4, 32), (48, 0, 16)]))
    # frame
    parts.append(f'<rect x="0" y="0" width="{W}" height="4" fill="#05070f"/><rect x="0" y="{H-4}" width="{W}" height="4" fill="#05070f"/>'
                 f'<rect x="0" y="0" width="4" height="{H}" fill="#05070f"/><rect x="{W-4}" y="0" width="4" height="{H}" fill="#05070f"/>')
    parts.append("</svg>")
    return "".join(parts)


def divider():
    w, h = 960, 24
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" shape-rendering="crispEdges">']
    rects = []
    period = 48
    for x0 in range(-period, w + period, period):
        rects += [f'<rect x="{x0}" y="12" width="16" height="4" fill="{FOAM}"/>',
                  f'<rect x="{x0+16}" y="8" width="16" height="4" fill="{FOAM}"/>',
                  f'<rect x="{x0+32}" y="12" width="8" height="4" fill="{FOAM}"/>',
                  f'<rect x="{x0}" y="16" width="{period}" height="8" fill="#14588c"/>']
    parts.append(f'<g><animateTransform attributeName="transform" type="translate" values="0 0;{-period} 0" dur="2.5s" repeatCount="indefinite"/>{"".join(rects)}</g>')
    parts.append("</svg>")
    return "".join(parts)


open(f"{OUT}/banner.svg", "w").write(banner())
open(f"{OUT}/divider.svg", "w").write(divider())
print("ok")
