from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "media" / "intro"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1280, 720
CREAM = "#F7F4E9"
INK = "#163A42"
DEEP = "#0D5961"
GREEN = "#168C69"
MINT = "#BDE8D5"
SKY = "#DFF1F0"
YELLOW = "#F2CB62"
WHITE = "#FFFFFF"
MUTED = "#385D63"

FONT_BOLD = "C:/Windows/Fonts/trebucbd.ttf"
FONT_SERIF = "C:/Windows/Fonts/georgiai.ttf"
FONT_BODY = "C:/Windows/Fonts/bahnschrift.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text(draw, xy, value, size, color=INK, bold=False, serif=False, anchor=None):
    path = FONT_SERIF if serif else (FONT_BOLD if bold else FONT_BODY)
    draw.text(xy, value, font=font(path, size), fill=color, anchor=anchor)


def wrap(draw, value, max_width, size, bold=False):
    words = value.split()
    lines, current = [], ""
    path = FONT_BOLD if bold else FONT_BODY
    fnt = font(path, size)
    for word in words:
        candidate = f"{current} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=fnt)[2] <= max_width:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def label(draw, value):
    draw.ellipse((72, 68, 90, 86), fill=GREEN)
    text(draw, (105, 77), value.upper(), 18, GREEN, bold=True, anchor="lm")


def footer(draw, number):
    text(draw, (72, 670), "ReLoop / CIRCULAR DEVICE SERVICE", 14, MUTED, bold=True)
    text(draw, (1208, 670), f"0{number} / 05", 14, MUTED, bold=True, anchor="ra")


def laptop(draw, x, y, scale=1.0):
    sw, sh = int(390 * scale), int(235 * scale)
    rounded(draw, (x, y, x + sw, y + sh), int(14 * scale), DEEP)
    rounded(
        draw,
        (x + int(15 * scale), y + int(15 * scale), x + sw - int(15 * scale), y + sh - int(23 * scale)),
        int(7 * scale),
        MINT,
    )
    draw.polygon(
        [
            (x - int(35 * scale), y + sh),
            (x + sw + int(35 * scale), y + sh),
            (x + sw + int(65 * scale), y + sh + int(22 * scale)),
            (x - int(65 * scale), y + sh + int(22 * scale)),
        ],
        fill="#CAD7D2",
    )
    text(draw, (x + sw // 2, y + sh // 2 - 3), "↻", int(92 * scale), DEEP, serif=True, anchor="mm")
    cx, cy = x + sw // 2, y + sh // 2 - int(3 * scale)
    radius = int(40 * scale)
    clear_radius = int(58 * scale)
    draw.rectangle(
        (cx - clear_radius, cy - clear_radius, cx + clear_radius, cy + clear_radius),
        fill=MINT,
    )
    draw.arc(
        (cx - radius + 7, cy - radius + 7, cx + radius - 7, cy + radius - 7),
        30,
        320,
        fill=DEEP,
        width=max(3, int(5 * scale)),
    )
    draw.polygon(
        [
            (cx + radius - int(11 * scale), cy - int(8 * scale)),
            (cx + radius, cy - int(3 * scale)),
            (cx + radius - int(9 * scale), cy + int(8 * scale)),
        ],
        fill=DEEP,
    )


def base(bg=CREAM):
    image = Image.new("RGB", (W, H), bg)
    return image, ImageDraw.Draw(image)


def scene_1():
    image, draw = base(DEEP)
    draw.ellipse((72, 68, 90, 86), fill=MINT)
    text(draw, (105, 77), "OUR VISION", 18, MINT, bold=True, anchor="lm")
    text(draw, (72, 145), "A future where every", 63, WHITE, bold=True)
    text(draw, (72, 225), "useful device gets", 68, WHITE, bold=True)
    text(draw, (72, 315), "another life.", 86, MINT, serif=True)
    text(draw, (74, 440), "Affordable technology. Less electronic waste.", 27, "#D2E7E5")
    draw.ellipse((815, 115, 1195, 495), fill=YELLOW)
    laptop(draw, 760, 235, 0.94)
    for radius in (245, 285):
        draw.arc((1005 - radius, 305 - radius, 1005 + radius, 305 + radius), 198, 515, fill=MINT, width=4)
    text(draw, (72, 670), "ReLoop / CIRCULAR DEVICE SERVICE", 14, "#B8D5D3", bold=True)
    text(draw, (1208, 670), "01 / 05", 14, "#B8D5D3", bold=True, anchor="ra")
    return image


def scene_2():
    image, draw = base(SKY)
    label(draw, "The challenge")
    text(draw, (72, 145), "Useful technology", 76, DEEP, bold=True)
    text(draw, (72, 228), "becomes waste.", 82, GREEN, serif=True)
    text(draw, (72, 340), "Organizations replace computers every few years,", 25, MUTED)
    text(draw, (72, 380), "even when many still have productive life left.", 25, MUTED)
    cards = [
        (742, 128, "REFRESH CYCLE", "3–5 years"),
        (925, 300, "USEFUL LIFE", "Still remaining"),
        (720, 482, "THE RESULT", "Electronic waste"),
    ]
    for x, y, title, sub in cards:
        rounded(draw, (x, y, x + 270, y + 118), 18, WHITE, DEEP, 2)
        draw.ellipse((x + 20, y + 23, x + 58, y + 61), fill=MINT)
        text(draw, (x + 75, y + 36), title, 16, GREEN, bold=True)
        text(draw, (x + 75, y + 73), sub, 24, INK, bold=True)
    draw.arc((860, 168, 1180, 533), 78, 278, fill=GREEN, width=7)
    draw.polygon([(1112, 516), (1138, 552), (1092, 548)], fill=GREEN)
    footer(draw, 2)
    return image


def scene_3():
    image, draw = base()
    label(draw, "Our solution")
    text(draw, (72, 145), "Recover. Renew.", 78, DEEP, bold=True)
    lines = ["Inspect", "Repair", "Grade", "Securely sanitize"]
    for index, item in enumerate(lines, start=1):
        y = 270 + (index - 1) * 68
        rounded(draw, (74, y - 9, 120, y + 37), 23, MINT)
        text(draw, (97, y + 14), f"{index}", 18, DEEP, bold=True, anchor="mm")
        text(draw, (142, y + 13), item, 27, MUTED, bold=True, anchor="lm")
    rounded(draw, (775, 102, 1175, 608), 10, WHITE, DEEP, 3)
    text(draw, (810, 142), "ReLoop DEVICE PASSPORT", 17, DEEP, bold=True)
    rounded(draw, (810, 180, 1140, 338), 7, MINT)
    text(draw, (975, 260), "RL", 56, DEEP, bold=True, anchor="mm")
    checks = [("DEVICE GRADE", "A"), ("HARDWARE TEST", "PASS"), ("RESIDUAL DATA", "ZERO")]
    for i, (key, value) in enumerate(checks):
        y = 390 + i * 65
        text(draw, (810, y), key, 15, MUTED, bold=True)
        text(draw, (1135, y), value, 18, GREEN, bold=True, anchor="ra")
        draw.line((810, y + 28, 1140, y + 28), fill="#CDD9D4", width=2)
    footer(draw, 3)
    return image


def scene_4():
    image, draw = base(SKY)
    label(draw, "Step three")
    text(draw, (72, 140), "Redeploy", 88, DEEP, bold=True)
    text(draw, (72, 235), "Reliable technology for teams", 29, MUTED)
    text(draw, (72, 275), "that make every dollar count.", 29, MUTED)
    customers = [
        ("SCHOOLS", "Student & staff devices", "#FFFDF5"),
        ("NONPROFITS", "Flexible quantities", DEEP),
        ("SMALL BUSINESS", "Predictable monthly costs", MINT),
    ]
    for index, (title, sub, color) in enumerate(customers):
        x = 70 + index * 405
        y = 380
        rounded(draw, (x, y, x + 365, y + 205), 20, color)
        title_color = WHITE if color == DEEP else DEEP
        sub_color = "#D2E7E5" if color == DEEP else MUTED
        draw.ellipse((x + 28, y + 30, x + 76, y + 78), fill=YELLOW)
        text(draw, (x + 95, y + 55), title, 18, title_color, bold=True, anchor="lm")
        for line_index, line in enumerate(wrap(draw, sub, 270, 22, True)):
            text(draw, (x + 30, y + 120 + line_index * 30), line, 22, sub_color, bold=True)
    footer(draw, 4)
    return image


def scene_5():
    image, draw = base(DEEP)
    draw.ellipse((820, 90, 1200, 470), fill=YELLOW)
    laptop(draw, 760, 230, 0.94)
    text(draw, (72, 110), "ReLoop", 40, MINT, bold=True)
    text(draw, (72, 218), "Return devices", 72, WHITE, bold=True)
    text(draw, (72, 302), "to the loop.", 80, MINT, serif=True)
    text(draw, (74, 430), "Maintain. Reuse. Responsibly recycle.", 26, "#D2E7E5")
    text(draw, (74, 472), "Keep useful technology in motion.", 26, "#D2E7E5")
    rounded(draw, (72, 545, 418, 610), 9, MINT)
    text(draw, (245, 577), "KEEP IT IN THE LOOP  →", 18, DEEP, bold=True, anchor="mm")
    rounded(draw, (72, 545, 418, 610), 9, MINT)
    text(draw, (245, 577), "KEEP IT IN THE LOOP", 18, DEEP, bold=True, anchor="mm")
    text(draw, (1208, 670), "ReLoop / SHAD STUDENT VENTURE", 14, "#B8D5D3", bold=True, anchor="ra")
    return image


def main():
    scenes = [scene_1(), scene_2(), scene_3(), scene_4(), scene_5()]
    for index, image in enumerate(scenes, start=1):
        image.save(OUT / f"scene-{index}.png", optimize=True)
    scenes[0].save(OUT / "poster.png", optimize=True)
    print(f"Generated {len(scenes)} scenes in {OUT}")


if __name__ == "__main__":
    main()
