"""Generates the site's illustrations (olfactory portraits) as SVG into assets/art/."""
import math, random, os
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "art")
os.makedirs(OUT, exist_ok=True)
SILVER = "#e6e2dc"; GOLD = "#d8c3a0"

def svg(w, h, body, defs=""):
    grain = ("<filter id='g'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/>"
             "<feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .09 0'/></filter>"
             "<filter id='blur'><feGaussianBlur stdDeviation='60'/></filter>"
             "<filter id='soft'><feGaussianBlur stdDeviation='18'/></filter>")
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}' width='{w}' height='{h}'>"
            f"<defs>{grain}{defs}</defs>{body}<rect width='{w}' height='{h}' filter='url(#g)'/></svg>")

def glow(blobs):
    return "<g filter='url(#blur)'>" + "".join(
        f"<circle cx='{x}' cy='{y}' r='{r}' fill='{c}' opacity='{o}'/>" for x, y, r, c, o in blobs) + "</g>"

def line(d, sw=1.4, c=SILVER, o=.9):
    return f"<path d='{d}' fill='none' stroke='{c}' stroke-width='{sw}' stroke-linecap='round' stroke-linejoin='round' opacity='{o}'/>"

def raspberry(cx, cy, s, c=SILVER):
    out = []
    for row, n in enumerate([3, 4, 5, 4, 3, 2]):
        for i in range(n):
            x = cx + (i - (n - 1) / 2) * s * 1.05
            y = cy + row * s * .92
            out.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='{s*.52:.1f}' fill='none' stroke='{c}' stroke-width='1.1' opacity='.85'/>")
    out.append(line(f"M{cx-s*1.6} {cy-s*.9} Q{cx} {cy-s*2.2} {cx+s*1.6} {cy-s*.9}", 1.1, GOLD))
    return "".join(out)

def passionfruit(cx, cy, r):
    out = [f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='none' stroke='{SILVER}' stroke-width='1.4'/>",
           f"<circle cx='{cx}' cy='{cy}' r='{r*.82}' fill='none' stroke='{GOLD}' stroke-width='.9' opacity='.8'/>"]
    rnd = random.Random(7)
    for _ in range(46):
        a = rnd.uniform(0, 2 * math.pi); d = r * .7 * math.sqrt(rnd.random())
        x, y = cx + d * math.cos(a), cy + d * math.sin(a)
        out.append(f"<ellipse cx='{x:.1f}' cy='{y:.1f}' rx='3.2' ry='4.6' transform='rotate({math.degrees(a):.0f} {x:.1f} {y:.1f})' fill='{SILVER}' opacity='.75'/>")
    return "".join(out)

def pear(cx, cy, s):
    d = (f"M{cx} {cy-s*1.3} C{cx+s*.35} {cy-s*1.3} {cx+s*.4} {cy-s*.55} {cx+s*.55} {cy-s*.2} "
         f"C{cx+s*1.05} {cy+s*.35} {cx+s*.95} {cy+s*1.2} {cx} {cy+s*1.2} "
         f"C{cx-s*.95} {cy+s*1.2} {cx-s*1.05} {cy+s*.35} {cx-s*.55} {cy-s*.2} "
         f"C{cx-s*.4} {cy-s*.55} {cx-s*.35} {cy-s*1.3} {cx} {cy-s*1.3}Z")
    return line(d) + line(f"M{cx} {cy-s*1.3} q{s*.08} {-s*.35} {s*.3} {-s*.5}", 1.4, GOLD)

def rose(cx, cy, r, c=SILVER):
    out = []
    for i in range(9):
        rr = r * (1 - i * .1); a0 = i * 47
        a1, a2 = math.radians(a0), math.radians(a0 + 250)
        x1, y1 = cx + rr * math.cos(a1), cy + rr * .86 * math.sin(a1)
        x2, y2 = cx + rr * math.cos(a2), cy + rr * .86 * math.sin(a2)
        out.append(line(f"M{x1:.1f} {y1:.1f} A{rr:.1f} {rr*.86:.1f} 0 1 1 {x2:.1f} {y2:.1f}", 1.3 - i * .06, c, .9))
    out.append(line(f"M{cx} {cy+r*.9} C{cx-r*.2} {cy+r*1.8} {cx+r*.25} {cy+r*2.4} {cx} {cy+r*3.2}", 1.3, GOLD))
    out.append(line(f"M{cx-r*.05} {cy+r*1.9} c{-r*.5} {-r*.1} {-r*.8} {r*.2} {-r*.9} {r*.5} c{r*.4} {r*.05} {r*.75} {-r*.1} {r*.9} {-r*.5}Z", 1.1, GOLD, .8))
    return "".join(out)

def peony(cx, cy, r):
    out = []
    for k in range(3):
        n = 7 + k * 2; rr = r * (1 - k * .27)
        for i in range(n):
            a = 2 * math.pi * i / n + k * .3
            px, py = cx + rr * .55 * math.cos(a), cy + rr * .55 * math.sin(a)
            out.append(f"<ellipse cx='{px:.1f}' cy='{py:.1f}' rx='{rr*.5:.1f}' ry='{rr*.28:.1f}' transform='rotate({math.degrees(a):.0f} {px:.1f} {py:.1f})' fill='none' stroke='{SILVER}' stroke-width='.9' opacity='{.55+k*.15:.2f}'/>")
    return "".join(out)

def lychee(cx, cy, r):
    out = [f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='none' stroke='{SILVER}' stroke-width='1.3'/>"]
    for i in range(0, 360, 30):
        for j in range(-60, 61, 30):
            a, b = math.radians(i), math.radians(j)
            x, y = cx + r * .75 * math.cos(a) * math.cos(b), cy + r * .75 * math.sin(b)
            out.append(f"<path d='M{x-4:.1f} {y:.1f} l4 -4 l4 4 l-4 4z' fill='none' stroke='{GOLD}' stroke-width='.7' opacity='.55'/>")
    return "".join(out)

def sand(w, y0, h, n=7):
    out = []
    for i in range(n):
        y = y0 + i * h / n
        d = f"M0 {y:.0f} " + " ".join(f"Q{w*(k+.5)/4:.0f} {y + (18 if k%2 else -18) + i*2:.0f} {w*(k+1)/4:.0f} {y:.0f}" for k in range(4))
        out.append(line(d, .9, GOLD, .25 + i * .07))
    return "".join(out)

def frame(w, h, title, sub):
    return (f"<rect x='28' y='28' width='{w-56}' height='{h-56}' fill='none' stroke='{SILVER}' stroke-width='.8' opacity='.35'/>"
            f"<text x='{w/2}' y='{h-78}' text-anchor='middle' fill='{SILVER}' font-family='Cormorant Garamond, Georgia, serif' font-style='italic' font-size='44' font-weight='300'>{title}</text>"
            f"<text x='{w/2}' y='{h-44}' text-anchor='middle' fill='{GOLD}' font-family='Josefin Sans, Helvetica, sans-serif' font-size='13' letter-spacing='6'>{sub}</text>")

W, H = 800, 1000
# 1. Fruits du Ciel: dusk sky over warm sand
fdc = svg(W, H,
  f"<rect width='{W}' height='{H}' fill='#120c0b'/>"
  + glow([(220, 260, 260, '#e58f6f', .55), (600, 200, 230, '#c9607a', .45), (420, 520, 300, '#f2b58a', .35), (400, 820, 360, '#6b4a2e', .5)])
  + sand(W, 690, 180)
  + passionfruit(270, 380, 105) + raspberry(560, 300, 22) + pear(560, 560, 78)
  + frame(W, H, "Fruits du Ciel", "PASSIONFRUIT · RASPBERRY · WARM SAND"))
# 2. Jardin d'Eden: night garden
jde = svg(W, H,
  f"<rect width='{W}' height='{H}' fill='#08100c'/>"
  + glow([(300, 330, 280, '#7a2e45', .55), (560, 560, 260, '#2f5a45', .5), (380, 760, 260, '#b5687d', .3)])
  + rose(330, 320, 120) + peony(580, 600, 120) + lychee(210, 640, 60)
  + frame(W, H, "Jardin d'Éden", "TURKISH ROSE · PEONY · LYCHEE"))
# 3. Istanbul at dusk (skyline line art)
sky = []
base = 640
sky.append(line(f"M0 {base} L800 {base}", 1, GOLD, .6))
def dome(cx, r): return f"M{cx-r} {base-60} A{r} {r} 0 0 1 {cx+r} {base-60}"
for cx, r in [(400, 95), (300, 50), (500, 50), (235, 28), (565, 28)]:
    sky.append(line(dome(cx, r), 1.3))
sky.append(line(f"M290 {base-60} L510 {base-60} L510 {base} L290 {base}Z", 1.1, SILVER, .7))
for x in (170, 630, 120, 680):
    hgt = 300 if x in (170, 630) else 250
    sky.append(line(f"M{x-6} {base} L{x-6} {base-hgt} L{x} {base-hgt-40} L{x+6} {base-hgt} L{x+6} {base}", 1.1))
    sky.append(line(f"M{x-11} {base-hgt+60} L{x+11} {base-hgt+60}", 1, GOLD))
for i in range(7):
    y = base + 30 + i * 26
    sky.append(line(f"M{60+i*20} {y} Q400 {y+8} {740-i*20} {y}", .8, SILVER, .5 - i * .06))
ist = svg(W, H, f"<rect width='{W}' height='{H}' fill='#0d0a10'/>"
  + glow([(400, 380, 330, '#c77a5c', .45), (180, 200, 220, '#5d3f6e', .4), (650, 240, 200, '#9c5b6a', .35)])
  + f"<circle cx='400' cy='300' r='60' fill='{GOLD}' opacity='.18'/>" + "".join(sky)
  + frame(W, H, "Istanbul", "WHERE THE HOUSE BEGAN · 2021"))
# 4. The Gift: ribboned box
gift = svg(W, H, f"<rect width='{W}' height='{H}' fill='#0c0b0a'/>"
  + glow([(400, 450, 300, '#a8865a', .35), (250, 700, 220, '#5a3a2a', .4)])
  + line("M240 420 L560 420 L560 700 L240 700Z", 1.4) + line("M220 360 L580 360 L580 420 L220 420Z", 1.4)
  + line("M400 360 L400 700", 2, GOLD) + line("M400 360 C340 270 260 300 300 345 C320 365 370 362 400 360", 1.5, GOLD)
  + line("M400 360 C460 270 540 300 500 345 C480 365 430 362 400 360", 1.5, GOLD)
  + line("M400 362 C380 400 360 430 330 470", 1.2, GOLD, .7) + line("M400 362 C420 400 440 430 470 470", 1.2, GOLD, .7)
  + frame(W, H, "The Gift", "A RITUAL OF GIVING"))
# 5. Notes study: ingredient constellation
rnd = random.Random(3)
stars = "".join(f"<circle cx='{rnd.uniform(60,740):.0f}' cy='{rnd.uniform(60,800):.0f}' r='{rnd.uniform(.6,1.8):.1f}' fill='{SILVER}' opacity='{rnd.uniform(.2,.8):.2f}'/>" for _ in range(160))
pts = [(170, 240, "Bergamot"), (330, 170, "Lychee"), (520, 230, "Rhubarb"), (620, 400, "Peony"), (420, 470, "Turkish Rose"),
       (230, 520, "Vanilla"), (330, 690, "Cashmeran"), (560, 650, "Vetiver"), (150, 720, "Musk")]
con = line("M" + " L".join(f"{x} {y}" for x, y, _ in pts), .8, GOLD, .5)
lbl = "".join(f"<circle cx='{x}' cy='{y}' r='4' fill='{GOLD}'/><text x='{x+12}' y='{y+5}' fill='{SILVER}' font-family='Cormorant Garamond, Georgia, serif' font-style='italic' font-size='22'>{t}</text>" for x, y, t in pts)
notes = svg(W, H, f"<rect width='{W}' height='{H}' fill='#07080c'/>" + glow([(400, 450, 340, '#3b3557', .45)]) + stars + con + lbl
  + frame(W, H, "A Constellation of Notes", "JARDIN D'ÉDEN · TOP TO BASE"))

for name, s in [("fruits-du-ciel", fdc), ("jardin-d-eden", jde), ("istanbul", ist), ("the-gift", gift), ("notes", notes)]:
    open(os.path.join(OUT, f"{name}.svg"), "w").write(s)
print("ok")
