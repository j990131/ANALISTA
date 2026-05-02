"""Generate a transparent-2026 overlay PNG.

Produces an image with an opaque black background and the text "2026"
knocked out (alpha = 0) so it can be layered over another image to let
the underlying content show through. "SEASON" is kept as gold text.
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

WIDTH, HEIGHT = 1200, 630
BG = (0, 0, 0, 255)           # opaque black
GOLD = (193, 154, 91, 255)    # warm gold for SEASON

YEAR_FONT_PATH = "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf"
LABEL_FONT_PATH = "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf"

YEAR_SIZE = 260
LABEL_SIZE = 56
LABEL_TRACKING = 18  # extra px between SEASON letters

OUT_PATH = Path(__file__).resolve().parent.parent / "Resources" / "2026_season_overlay.png"


def draw_tracked_text(draw, xy, text, font, fill, tracking):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        bbox = font.getbbox(ch)
        x += (bbox[2] - bbox[0]) + tracking


def measure_tracked(font, text, tracking):
    width = 0
    for ch in text:
        bbox = font.getbbox(ch)
        width += (bbox[2] - bbox[0]) + tracking
    return max(0, width - tracking)


def main():
    img = Image.new("RGBA", (WIDTH, HEIGHT), BG)

    year_font = ImageFont.truetype(YEAR_FONT_PATH, YEAR_SIZE)
    label_font = ImageFont.truetype(LABEL_FONT_PATH, LABEL_SIZE)

    year_text = "2026"
    label_text = "SEASON"

    yb = year_font.getbbox(year_text)
    year_w = yb[2] - yb[0]
    year_h = yb[3] - yb[1]
    year_x = (WIDTH - year_w) // 2 - yb[0]
    year_y = (HEIGHT - year_h) // 2 - yb[1] - 40

    label_w = measure_tracked(label_font, label_text, LABEL_TRACKING)
    label_x = (WIDTH - label_w) // 2
    label_y = year_y + year_h + 30

    # 1) draw SEASON in gold (stays opaque)
    draw = ImageDraw.Draw(img)
    draw_tracked_text(draw, (label_x, label_y), label_text, label_font, GOLD, LABEL_TRACKING)

    # 2) knock out 2026 by drawing it directly into the alpha channel as 0
    mask = Image.new("L", (WIDTH, HEIGHT), 255)  # 255 = keep, 0 = cut
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.text((year_x, year_y), year_text, font=year_font, fill=0)

    # apply mask to alpha
    r, g, b, a = img.split()
    new_alpha = Image.eval(mask, lambda v: v).point(lambda v: v)
    # combine: where mask is 0, alpha becomes 0; otherwise keep current alpha
    combined_alpha = Image.eval(a, lambda v: v)
    combined_alpha = Image.composite(combined_alpha, Image.new("L", (WIDTH, HEIGHT), 0), mask)
    img.putalpha(combined_alpha)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH, "PNG")
    print(f"wrote {OUT_PATH}  ({WIDTH}x{HEIGHT})")


if __name__ == "__main__":
    main()
