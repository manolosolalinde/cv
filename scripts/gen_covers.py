#!/usr/bin/env python3
"""Generate data-free placeholder cover images (1200x675) for project cards.

Matches the ORIGINAL covers/ technique (surveillance/plunger/gas_injection):
  - 2x supersampling + LANCZOS downscale for smooth, anti-aliased strokes
  - a per-project background gradient (distinct mood per card)
  - a bottom scrim for title legibility, with the accent bar drawn AFTER the
    scrim so it stays visible
  - bold DejaVu title + subtitle bottom-left

Each new card gets its own palette so the set doesn't look templated. All art
is abstract/illustrative — no client data.
"""
import math
import random

from PIL import Image, ImageDraw, ImageFont

S = 2  # supersample factor for smooth lines
W, H = 1200, 675
CW, CH = W * S, H * S
COVERS = "projects/images/covers"


def P(v):
    return int(round(v * S))


def font(size, bold=True):
    path = ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
            else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    try:
        return ImageFont.truetype(path, size * S)
    except Exception:
        return ImageFont.load_default()


def hexc(s):
    s = s.lstrip("#")
    return tuple(int(s[i:i + 2], 16) for i in (0, 2, 4))


def vgrad(draw, top, bot):
    for y in range(CH):
        t = y / CH
        c = tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3))
        draw.line([(0, y), (CW, y)], fill=c)


# ----------------------------------------------------------------------------
# Motifs (display coordinates; scaled to the supersampled canvas via P()).
# ----------------------------------------------------------------------------
def panel(d, box):
    d.rounded_rectangle([P(box[0]), P(box[1]), P(box[2]), P(box[3])],
                        radius=14 * S, fill=(255, 255, 255))


def line_chart(d, box, color, seed, width=4, n=24):
    x0, y0, x1, y1 = box
    random.seed(seed)
    w, h = x1 - x0, y1 - y0
    base, amp = y1 - 14, h - 28
    v = random.uniform(0.3, 0.7)
    pts = []
    for i in range(n):
        v = min(1, max(0, v + random.uniform(-0.18, 0.2)))
        px = x0 + 12 + i * ((w - 24) / (n - 1))
        py = base - amp * v
        pts.append((P(px), P(py)))
    d.line(pts, fill=color, width=int(width * S), joint="curve")


def bar_chart(d, box, color, seed, n=18):
    x0, y0, x1, y1 = box
    random.seed(seed)
    w, h = x1 - x0, y1 - y0
    bw = (w - 28) / n * 0.55
    for i in range(n):
        bx = x0 + 14 + i * ((w - 28) / n)
        bh = random.uniform(0.2, 1.0) * (h - 28)
        d.rounded_rectangle([P(bx), P((y1 - 14) - bh), P(bx + bw), P(y1 - 14)],
                            radius=3 * S, fill=color)


def scatter(d, box, color, seed, n=24):
    x0, y0, x1, y1 = box
    random.seed(seed)
    for _ in range(n):
        px = random.uniform(x0 + 20, x1 - 20)
        py = random.uniform(y0 + 20, y1 - 20)
        r = random.uniform(4, 8)
        d.ellipse([P(px - r), P(py - r), P(px + r), P(py + r)], fill=color)


def contour(d, box, color):
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    maxr = min(x1 - x0, y1 - y0) / 2 - 18
    rings = 6
    for i in range(rings, 0, -1):
        r = maxr * i / rings
        shade = tuple(int(c + (255 - c) * (1 - i / rings) * 0.75) for c in color)
        d.ellipse([P(cx - r), P(cy - r * 0.72), P(cx + r), P(cy + r * 0.72)],
                  outline=shade, width=int(4 * S))


def chat_bubbles(d, box, accent, seed):
    x0, y0, x1, y1 = box
    random.seed(seed)
    pad = 28
    x0 += pad; y0 += pad; x1 -= pad; y1 -= pad
    rows = 4
    rh = (y1 - y0) / rows
    y = y0
    for i in range(rows):
        right = i % 2 == 1
        w = random.uniform(0.45, 0.8) * (x1 - x0)
        bh = rh * 0.6
        if right:
            bx0, bx1, fill = x1 - w, x1, accent
        else:
            bx0, bx1, fill = x0, x0 + w, (214, 222, 233)
        d.rounded_rectangle([P(bx0), P(y), P(bx1), P(y + bh)], radius=12 * S, fill=fill)
        y += rh


def blocks(d, box, color, seed, rows=4):
    x0, y0, x1, y1 = box
    random.seed(seed)
    pad = 20
    x0 += pad; y0 += pad; x1 -= pad; y1 -= pad
    rh = (y1 - y0) / rows
    for i in range(rows):
        by = y0 + rh * i
        inset = random.uniform(0, 0.1) * (x1 - x0)
        shade = tuple(int(c + (255 - c) * (i / rows) * 0.5) for c in color)
        d.rounded_rectangle([P(x0 + inset), P(by + 6), P(x1 - inset), P(by + rh - 6)],
                            radius=8 * S, fill=shade)


# ----------------------------------------------------------------------------
# Finish: scrim -> accent bar (on top) -> title/subtitle -> downscale.
# ----------------------------------------------------------------------------
def finish(img, name, title, subtitle, accent):
    scrim = Image.new("RGBA", (CW, 230 * S), (0, 0, 0, 0))
    sd = ImageDraw.Draw(scrim)
    for y in range(230 * S):
        a = int(200 * (y / (230 * S)))
        sd.line([(0, y), (CW, y)], fill=(8, 12, 20, a))
    img.paste(scrim, (0, CH - 230 * S), scrim)

    d = ImageDraw.Draw(img)
    d.rectangle([0, CH - 12 * S, CW, CH], fill=accent)  # accent bar ON TOP of scrim

    size = 46
    tf = font(size)
    while d.textlength(title, font=tf) > CW - 140 * S and size > 34:
        size -= 2
        tf = font(size)
    d.text((70 * S, CH - 150 * S), title, font=tf, fill="#f8fafc")
    d.text((70 * S, CH - 90 * S), subtitle, font=font(24, bold=False), fill="#cbd5e1")

    out = img.resize((W, H), Image.LANCZOS)
    out.save(f"{COVERS}/{name}.png", optimize=True)
    print("wrote", name, out.size)


# ----------------------------------------------------------------------------
# Layouts.
# ----------------------------------------------------------------------------
def dashboard(d, accent, seed):
    purple, green = hexc("#818cf8"), hexc("#34d399")
    pink, amber = hexc("#f472b6"), hexc("#fbbf24")
    tiles = [(70, 70, 540, 330), (580, 70, 1130, 210), (580, 250, 1130, 330),
             (70, 360, 380, 560), (420, 360, 760, 560), (800, 360, 1130, 560)]
    panel(d, tiles[0]); line_chart(d, tiles[0], accent, seed + 1)
    panel(d, tiles[1]); line_chart(d, tiles[1], accent, seed + 2)
    panel(d, tiles[2]); bar_chart(d, tiles[2], purple, seed + 3)
    panel(d, tiles[3]); scatter(d, tiles[3], green, seed + 4)
    panel(d, tiles[4]); line_chart(d, tiles[4], pink, seed + 5)
    panel(d, tiles[5]); line_chart(d, tiles[5], amber, seed + 6)


def agent_layout(d, accent, seed):
    panel(d, (70, 70, 690, 560)); chat_bubbles(d, (70, 70, 690, 560), accent, seed)
    panel(d, (730, 70, 1130, 300)); line_chart(d, (730, 70, 1130, 300), accent, seed + 2)
    panel(d, (730, 320, 1130, 560)); bar_chart(d, (730, 320, 1130, 560), hexc("#818cf8"), seed + 3)


def contour_layout(d, accent, seed):
    panel(d, (70, 70, 600, 560)); contour(d, (70, 70, 600, 560), accent)
    panel(d, (640, 70, 1130, 300)); line_chart(d, (640, 70, 1130, 300), accent, seed + 2)
    panel(d, (640, 320, 1130, 560)); scatter(d, (640, 320, 1130, 560), hexc("#34d399"), seed + 3)


def infra_layout(d, accent, seed):
    panel(d, (70, 70, 520, 560)); blocks(d, (70, 70, 520, 560), accent, seed)
    panel(d, (560, 70, 1130, 300)); blocks(d, (560, 70, 1130, 300), hexc("#818cf8"), seed + 2)
    panel(d, (560, 320, 1130, 560)); line_chart(d, (560, 320, 1130, 560), accent, seed + 3)


LAYOUTS = {"dashboard": dashboard, "agent": agent_layout,
           "contour": contour_layout, "infra": infra_layout}


def build(name, title, subtitle, top, bot, accent, kind, seed):
    img = Image.new("RGB", (CW, CH))
    d = ImageDraw.Draw(img)
    vgrad(d, hexc(top), hexc(bot))
    acc = hexc(accent)
    LAYOUTS[kind](d, acc, seed)
    finish(img, name, title, subtitle, acc)


# ----------------------------------------------------------------------------
# The six cards. Each has its own gradient + accent for a distinct mood.
# ----------------------------------------------------------------------------
build("agent", "AI Agent Chat", "Conversational AI over operational well data",
      "#0a1626", "#0f2742", "#38bdf8", "agent", 11)

build("gas_targets", "Gas Targets App", "Monthly gas-production targets at fleet scale",
      "#0b0e24", "#1a1d40", "#6366f1", "dashboard", 21)

build("streamlit_apps", "BKV Streamlit Apps", "Reservoir & production engineering toolkit",
      "#120a22", "#271444", "#a78bfa", "contour", 51)

build("pulumi_templates", "Pulumi Templates", "Infrastructure-as-code for AWS ECS Fargate",
      "#160a20", "#2c1142", "#c084fc", "infra", 61)

print("done")
