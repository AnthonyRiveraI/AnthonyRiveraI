"""Pixel-art RPG inventory panels for the tech stack, quest log and contact buttons.

Run: python3 scripts/pixel_inventory.py  (also regenerates the banner)
"""
from pixel_banner import FONT, text_rects, sprite, OUT, GOLD, CREAM, FOAM

FONT.update({
    "J": ["00111", "00010", "00010", "00010", "00010", "10010", "01100"],
    "Q": ["01110", "10001", "10001", "10001", "10101", "10010", "01101"],
    "Z": ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
    "8": ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    "0": ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    "2": ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
    ".": ["00000", "00000", "00000", "00000", "00000", "01100", "01100"],
    "&": ["01100", "10010", "10100", "01000", "10101", "10010", "01101"],
    "/": ["00001", "00010", "00010", "00100", "01000", "01000", "10000"],
    "-": ["00000", "00000", "00000", "11111", "00000", "00000", "00000"],
    ":": ["00000", "01100", "01100", "00000", "01100", "01100", "00000"],
})

# ---------- 10x10 icons: (rows, palette) ----------
ICONS = {
    "claude": (["....oo....", ".o..oo..o.", "..o.oo.o..", "...oooo...", "oooooooooo",
                "oooooooooo", "...oooo...", "..o.oo.o..", ".o..oo..o.", "....oo...."],
               {"o": "#d97757"}),
    "gemini": (["....bb....", "....bb....", "...bbpp...", "..bbbppp..", "bbbbbppppp",
                "bbbbbppppp", "..bbbppp..", "...bbpp...", "....pp....", "....pp...."],
               {"b": "#4f8df5", "p": "#9b72f2"}),
    "openai": (["...gggg...", "..g....g..", ".g..gg..g.", "g..g..g..g", "g.g....g.g",
                "g.g....g.g", "g..g..g..g", ".g..gg..g.", "..g....g..", "...gggg..."],
               {"g": "#e8e8e8"}),
    "ollama": ([".w....w...", ".w....w...", ".wwwwww...", "wwwwwwww..", "wwdwwdww..",
                "wwwwwwww..", ".wwddww...", ".wwwwww...", "..wwww....", "..wwww...."],
               {"w": "#f4f4f4", "d": "#14141c"}, 1),
    "hf": (["..yyyyyy..", ".yyyyyyyy.", "yyydyydyyy", "yyydyydyyy", "yyyyyyyyyy",
            "ydyyyyyydy", "yyddddddyy", ".yyddddyy.", "oo.yyyy.oo", "oo......oo"],
           {"y": "#ffd21e", "d": "#3a2a0a", "o": "#ff9d00"}),
    "openrouter": ([".......cc.", "......cccc", ".....c.cc.", "....c.....", "cccc......",
                    "cccc......", "....c.....", ".....c.cc.", "......cccc", ".......cc."],
                   {"c": "#6ee7f9"}),
    "chip_glm": (["..g.g.g.g.", ".gggggggg.", "ggaaaaaagg", ".gaggggag.", "ggaggggagg",
                  ".gaggggag.", "ggaaaaaagg", ".gggggggg.", "..g.g.g.g.", ".........."],
                 {"g": "#8a93b8", "a": "#4f8df5"}),
    "chip_minimax": (["..g.g.g.g.", ".gggggggg.", "ggaaaaaagg", ".gaggggag.", "ggaggggagg",
                      ".gaggggag.", "ggaaaaaagg", ".gggggggg.", "..g.g.g.g.", ".........."],
                     {"g": "#8a93b8", "a": "#e2445c"}),
    "langchain": ([".........", "cccc......", "c..c......", "c..cccc...", "cccc..c...",
                   "...c..cccc", "...cccc..c", "......c..c", "......cccc", ".........."],
                  {"c": "#2dd4bf"}),
    "langgraph": (["nn.....nn.", "nn.....nn.", "..l...l...", "...l.l....", "....nn....",
                   "....nn....", "....l.....", "....l.....", "...nnnn...", "...nnnn..."],
                  {"n": "#2dd4bf", "l": "#9fd3f0"}),
    "adk": (["....aa....", "....aa....", ".bbbbbbbb.", ".bwwbbwwb.", ".bwwbbwwb.",
             ".bbbbbbbb.", ".bbaaaabb.", ".bbbbbbbb.", "..b....b..", "..b....b.."],
            {"b": "#4285f4", "w": "#ffffff", "a": "#fbbc05"}),
    "mcp": (["...p..p...", "...p..p...", "..pppppp..", "..pppppp..", "..pppppp..",
             "...pppp...", "....pp....", "....pp....", "....pp....", ".........."],
            {"p": "#e8e8e8"}),
    "claudecode": (["kkkkkkkkkk", "kddddddddk", "kdoddddddk", "kddodddddk", "kdoddddddk",
                    "kddddooodk", "kddddddddk", "kkkkkkkkkk"],
                   {"k": "#8a93b8", "d": "#14141c", "o": "#d97757"}, 1),
    "n8n": ([".......pp.", ".......pp.", "......l...", "pp...l....", "ppllpp....",
             "....pp....", ".....l....", "......l...", ".......pp.", ".......pp."],
            {"p": "#ea4b71", "l": "#f7a8bb"}),
    "postgres": (["..bbbbbb..", ".bllllllb.", ".bbbbbbbb.", ".bllllllb.", ".bbbbbbbb.",
                  ".bllllllb.", ".bbbbbbbb.", ".bllllllb.", "..bbbbbb.."],
                 {"b": "#336791", "l": "#6aa0d8"}),
    "supabase": ([".....gg...", "....ggg...", "...gggg...", "..ggggg...", ".gggggggg.",
                  "....gggg..", "....ggg...", "....gg....", "....g.....", ".........."],
                 {"g": "#3ecf8e"}),
    "pinecone": (["....c.....", "...ccc....", "..c.c.c...", ".ccc.ccc..", "..c.c.c...",
                  ".ccc.ccc..", "..c.c.c...", "...ccc....", "....c.....", "....c....."],
                 {"c": "#f4ecd8"}, 1),
    "qdrant": (["...qqqq...", "..qqqqqq..", ".qqq..qqq.", ".qq....qq.", ".qq....qq.",
                ".qqq..qqq.", "..qqqqqq..", "...qqqq...", "......qq..", ".......q.."],
               {"q": "#dc244c"}),
    "weaviate": (["w...w...w.", "..........", "..w...g...", "..........", "w...g...g.",
                  "..........", "..g...g...", "..........", "g...g...w."],
                 {"w": "#9fd3f0", "g": "#a3e635"}),
    "chroma": ([".........", "..........", ".yyy..bbb.", "yyyyyrbbbb", "yyyyrrrbbb",
                "yyyyyrbbbb", ".yyy..bbb.", ".........."],
               {"y": "#ffde2d", "b": "#327eff", "r": "#ff6446"}),
    "faiss": ([".mmmm.....", "m....m....", "m....m....", "m....m....", "m....m....",
               ".mmmm.....", ".....mm...", "......mm..", ".......mm.", ".........."],
              {"m": "#9fd3f0"}),
    "python": (["...bbbb...", "...b.bb...", ".....bb...", ".bbbbbb.y.", "bbbbbbb.yy",
                "bb.yyyyyyy", ".b.yyyyyy.", "...yy.....", "...yy.y...", "...yyyy..."],
               {"b": "#4b8bbe", "y": "#ffd43b"}),
    "fastapi": (["...tttt...", ".tttttttt.", ".tttttwwt.", "ttttwwwttt", "tttwwwwwtt",
                 "ttwwwwwttt", "tttwwwtttt", ".twwttttt.", ".tttttttt.", "...tttt..."],
                {"t": "#009688", "w": "#ffffff"}),
    "typescript": (["bbbbbbbbbb", "bbbbbbbbbb", "bwwwbbwwwb", "bbwbbwbbbb", "bbwbbbwwbb",
                    "bbwbbbbbwb", "bbwbbwwwbb", "bbbbbbbbbb", "bbbbbbbbbb", "bbbbbbbbbb"],
                   {"b": "#3178c6", "w": "#ffffff"}),
    "node": (["....gg....", "..gggggg..", "gggggggggg", "ggg....ggg", "ggg....ggg",
              "ggg....ggg", "ggg....ggg", "gggggggggg", "..gggggg..", "....gg...."],
             {"g": "#5fa04e"}),
    "next": (["..wwwwww..", ".wwwwwwww.", "wwkwwwkwww", "wwkkwwkwww", "wwkwkwkwww",
              "wwkwwkkwww", "wwkwwwkwww", ".wwwwwwww.", "..wwwwww.."],
             {"w": "#f4f4f4", "k": "#0b1026"}),
    "gcp": (["...rrrr...", "..r....b..", ".r......b.", "yy......bb", "y........b",
             "y........b", ".ggggbbbb."],
            {"r": "#ea4335", "y": "#fbbc05", "g": "#34a853", "b": "#4285f4"}, 1),
    "aws": (["...ssss...", ".ssssssss.", "ssssssssss", ".ssssssss.", "..........",
             ".o......o.", "..oooooo.o", "........oo"],
            {"s": "#c9d6ff", "o": "#ff9900"}, 1),
    "azure": (["....aa....", "...aaaa...", "...aaaa...", "..aa..aa..", "..aa..aa..",
               ".aaaaaaaa.", ".aa....aa.", "aa......aa"],
              {"a": "#0089d6"}, 1),
    "docker": ([".....cc...", "..cc.cc...", "cc.cc.cc..", "bbbbbbbbb.", "bbbbbbbbbb",
                ".bbwbbbbb.", "..bbbbbb.."],
               {"c": "#7cc4f7", "b": "#2496ed", "w": "#ffffff"}, 1),
    "k8s": (["...kkkk...", ".kkkwwkkk.", ".kwkwwkwk.", "kkkwwwwkkk", "kwwwkkwwwk",
             "kkkwwwwkkk", ".kwkwwkwk.", ".kkkwwkkk.", "...kkkk..."],
            {"k": "#326ce5", "w": "#ffffff"}),
    "linux": (["...kkkk...", "..kkkkkk..", "..kwkkwk..", "..kkyykk..", ".kkwwwwkk.",
               "kkwwwwwwkk", "kkwwwwwwkk", ".kwwwwwwk.", ".yyy..yyy."],
              {"k": "#14141c", "w": "#f4f4f4", "y": "#f2c94c"}),
    "git": (["....oo....", "...oooo...", "..owoooo..", ".oowwoooo.", "oooowwwooo",
             "oooowowwoo", ".ooowoooo.", "..owoooo..", "...oooo...", "....oo...."],
            {"o": "#f05033", "w": "#ffffff"}),
    "mic": (["...mmmm...", "...mwwm...", "...mmmm...", "...mmmm...", ".k.mmmm.k.",
             ".k..mm..k.", "..k....k..", "...kkkk...", "....kk....", "...kkkk..."],
            {"m": "#d97757", "w": "#ffd8c2", "k": "#c9d6ff"}),
    "vectors": (["c.........", "c....y....", "c.......p.", "c..p......", "c......y..",
                 "c.y..p....", "c.........", "cccccccccc"],
                {"c": "#8a93b8", "y": GOLD, "p": "#6ee7f9"}, 1),
    # quest icons
    "q_evals": (["wwwwwww...", "w.....w...", "w.ggg.w...", "w.....w...", "w.ggg.w..g",
                 "w.....w.gg", "w.ggg.wgg.", "w.....gg..", "wwwwwww...", ".........."],
                {"w": CREAM, "g": "#7ee081"}),
    "q_trace": (["k.........", "k......y..", "k.....y.y.", "k..y.y...y", "k.y.y.....",
                 "ky........", "k.........", "kkkkkkkkkk"],
                {"k": "#8a93b8", "y": GOLD}, 1),
    "q_guard": (["bbbbbbbbbb", "bwwwwwwwwb", "bwwwwgwwwb", "bwwwggwwwb", "bwwgwggwwb",
                 ".bwwwwwwb.", ".bwwwwwwb.", "..bwwwwb..", "...bwwb...", "....bb...."],
                {"b": "#4f8df5", "w": "#d6e4ff", "g": "#2a5bd7"}),
    "q_coin": (["...yyyy...", ".yyyyyyyy.", ".yyoyyoyy.", "yyyoooooyy", "yyyyoyyyyy",
                "yyyyyoyyyy", "yyoooooyyy", ".yyoyyoyy.", ".yyyyyyyy.", "...yyyy..."],
               {"y": GOLD, "o": "#a0731c"}),
}

NAVY, SLOT, HI, LO, FRAME = "#0b1026", "#18244d", "#2c3a73", "#05070f", "#d9a441"
W = 960
COLS, SW, SH, GAP, M = 4, 228, 56, 8, 12


def icon_svg(key, x, y, s=4):
    spec = ICONS[key]
    rows, pal = spec[0], spec[1]
    oy = (10 - len(rows)) * s // 2
    ox = (10 - max(len(r) for r in rows)) * s // 2
    return sprite(rows, pal, x + ox, y + oy, s)


def frame(w, h):
    return (f'<rect x="0" y="0" width="{w}" height="{h}" fill="{NAVY}"/>'
            f'<rect x="0" y="0" width="{w}" height="4" fill="{FRAME}"/><rect x="0" y="{h-4}" width="{w}" height="4" fill="{FRAME}"/>'
            f'<rect x="0" y="0" width="4" height="{h}" fill="{FRAME}"/><rect x="{w-4}" y="0" width="4" height="{h}" fill="{FRAME}"/>'
            f'<rect x="4" y="4" width="{w-8}" height="4" fill="#7a5a1c"/>'
            # pixel-notched corners
            f'<rect x="0" y="0" width="4" height="4" fill="{LO}"/><rect x="{w-4}" y="0" width="4" height="4" fill="{LO}"/>'
            f'<rect x="0" y="{h-4}" width="4" height="4" fill="{LO}"/><rect x="{w-4}" y="{h-4}" width="4" height="4" fill="{LO}"/>')


def header(title, h):
    return (text_rects(title, M + 8 + 2, 18 + 2, 3, LO) + text_rects(title, M + 8, 18, 3, GOLD))


def slot(x, y, w, h):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{SLOT}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="4" fill="{HI}"/><rect x="{x}" y="{y}" width="4" height="{h}" fill="{HI}"/>'
            f'<rect x="{x}" y="{y+h-4}" width="{w}" height="4" fill="{LO}"/><rect x="{x+w-4}" y="{y}" width="4" height="{h}" fill="{LO}"/>')


def panel(name, title, items):
    rows = (len(items) + COLS - 1) // COLS
    top = 52
    h = top + rows * SH + (rows - 1) * GAP + M + 4
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" shape-rendering="crispEdges">',
           f'<title>{title.title().replace("&", "&amp;")}</title>', frame(W, h), header(title, h)]
    for i, (key, label) in enumerate(items):
        r, c = divmod(i, COLS)
        x, y = M + c * (SW + GAP), top + r * (SH + GAP)
        out.append(slot(x, y, SW, SH))
        begin = (i * 0.37) % 2.4
        out.append(f'<g>{icon_svg(key, x + 10, y + 8)}'
                   f'<animateTransform attributeName="transform" type="translate" values="0 0;0 -2;0 0;0 0" '
                   f'keyTimes="0;0.15;0.3;1" calcMode="discrete" dur="2.4s" begin="{begin:.2f}s" repeatCount="indefinite"/></g>')
        out.append(text_rects(label, x + 60, y + 21, 2, CREAM))
    out.append("</svg>")
    open(f"{OUT}/{name}.svg", "w").write("".join(out))


def quests():
    items = [("q_evals", "EVALS", "GOLDEN SETS + LLM-AS-JUDGE"),
             ("q_trace", "TRACING", "LANGSMITH / LANGFUSE / OTEL"),
             ("q_guard", "GUARDRAILS", "PROMPT INJECTION + PII"),
             ("q_coin", "COST & LATENCY", "ROUTING + CACHING")]
    top, rh = 52, 64
    h = top + len(items) * (rh + GAP) - GAP + M + 4
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" shape-rendering="crispEdges">',
           '<title>Quest Log</title>', frame(W, h), header("QUEST LOG: LEVELING UP", h)]
    bx, bw = 640, 288
    for i, (key, name, sub) in enumerate(items):
        x, y = M, top + i * (rh + GAP)
        out.append(slot(x, y, W - 2 * M, rh))
        out.append(icon_svg(key, x + 12, y + 12))
        out.append(text_rects(name, x + 64, y + 12, 3, GOLD))
        out.append(text_rects(sub, x + 64, y + 40, 2, FOAM))
        # animated XP bar (charging loop, staggered)
        by = y + 22
        out.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="20" fill="{LO}"/>'
                   f'<rect x="{bx+4}" y="{by+4}" width="{bw-8}" height="12" fill="#1b2550"/>')
        steps = [str(4 + k * 20) for k in range(0, 15)]
        vals = ";".join(steps + [steps[-1]] * 4)
        out.append(f'<rect x="{bx+4}" y="{by+4}" width="4" height="12" fill="#7ee081">'
                   f'<animate attributeName="width" values="{vals}" calcMode="discrete" dur="4.8s" begin="{i*0.6}s" repeatCount="indefinite"/></rect>')
        out.append(f'<rect x="{bx+4}" y="{by+4}" width="{bw-8}" height="4" fill="#ffffff" opacity="0.12"/>')
    out.append("</svg>")
    open(f"{OUT}/quests.svg", "w").write("".join(out))


panel("stack-llms", "LLMS & PROVIDERS", [
    ("openai", "OPENAI"), ("claude", "CLAUDE"), ("gemini", "GEMINI"), ("ollama", "OLLAMA"),
    ("hf", "HUGGING FACE"), ("openrouter", "OPENROUTER"), ("chip_glm", "GLM"), ("chip_minimax", "MINIMAX")])
panel("stack-agents", "AGENTS & ORCHESTRATION", [
    ("langchain", "LANGCHAIN"), ("langgraph", "LANGGRAPH"), ("adk", "GOOGLE ADK"), ("mcp", "MCP"),
    ("claudecode", "CLAUDE CODE"), ("n8n", "N8N"), ("python", "PY HARNESSES"), ("mic", "REALTIME APIS")])
panel("stack-rag", "RAG & VECTOR STORES", [
    ("postgres", "PGVECTOR"), ("supabase", "SUPABASE"), ("pinecone", "PINECONE"), ("qdrant", "QDRANT"),
    ("weaviate", "WEAVIATE"), ("chroma", "CHROMA"), ("faiss", "FAISS"), ("vectors", "EMBEDDINGS")])
panel("stack-cloud", "BACKEND + CLOUD + DEVOPS", [
    ("python", "PYTHON"), ("fastapi", "FASTAPI"), ("typescript", "TYPESCRIPT"), ("node", "NODE.JS"),
    ("next", "NEXT.JS"), ("gcp", "GOOGLE CLOUD"), ("aws", "AWS"), ("azure", "AZURE"),
    ("docker", "DOCKER"), ("k8s", "KUBERNETES"), ("linux", "LINUX"), ("git", "GIT")])
quests()
print("inventory ok")


def button(name, key, label):
    w, h = 232, 56
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" shape-rendering="crispEdges">',
           f'<title>{label.title()}</title>', frame(w, h), slot(8, 8, w - 16, h - 16),
           icon_svg(key, 18, 8 + (h - 16 - 40) // 2),
           text_rects(label, 68, 21, 2, CREAM),
           f'<rect x="{w-30}" y="22" width="4" height="12" fill="{GOLD}"><animate attributeName="opacity" values="1;0" dur="1s" calcMode="discrete" repeatCount="indefinite"/></rect>',
           "</svg>"]
    open(f"{OUT}/{name}.svg", "w").write("".join(out))


ICONS["linkedin"] = (["bbbbbbbbbb", "bwwbbbbbbb", "bwwbbbbbbb", "bbbbbbbbbb", "bwwbwwbwwb",
                      "bwwbwwwwwb", "bwwbwwbwwb", "bwwbwwbwwb", "bwwbwwbwwb", "bbbbbbbbbb"],
                     {"b": "#0a66c2", "w": "#ffffff"})
ICONS["mail"] = (["wwwwwwwwww", "wrwwwwwwrw", "wwrwwwwrww", "wwwrwwrwww", "wwwwrrwwww",
                  "wwwwwwwwww", "wwwwwwwwww"],
                 {"w": CREAM, "r": "#d64545"}, 1)
button("btn-linkedin", "linkedin", "LINKEDIN")
button("btn-email", "mail", "EMAIL ME")
print("buttons ok")
