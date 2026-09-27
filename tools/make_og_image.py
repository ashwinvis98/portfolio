"""Generate the site-wide Open Graph card at static/og-default.png.

Design (per the brief): warm off-white ground, tagline in IBM Plex Serif,
name beneath in IBM Plex Mono. No photo, no logo, no gradient.

Sizing note: social platforms downscale a 1200x630 card to roughly 500px wide
in-feed, so small/low-contrast text turns to mush. The name line is therefore
set larger and darker than a print-style secondary line would be.

Usage:  python tools/make_og_image.py
Fonts are downloaded to a cache dir on first run; nothing is committed.
"""

from pathlib import Path
from urllib.request import urlopen

from PIL import Image, ImageDraw, ImageFont

# --- canvas -----------------------------------------------------------------
WIDTH, HEIGHT = 1200, 630
BG = "#FBFAF7"          # warm off-white
INK = "#1F1F1C"         # tagline
NAME_INK = "#57564F"    # name: darker than before so it survives downscaling

MARGIN_X = 92
TAGLINE_TOP = 178
TAGLINE_SIZE = 76
TAGLINE_LEADING = 100
NAME_SIZE = 36          # was 28 - too small once the card is shrunk in-feed
NAME_TOP = 424

TAGLINE = ["I build systems that make", "security teams effective."]
NAME = "Ashwin Viswamithiran"

# --- fonts ------------------------------------------------------------------
FONT_BASE = "https://cdn.jsdelivr.net/gh/IBM/plex@v5.1.3/IBM-Plex-{fam}/fonts/complete/ttf/{file}"
FONTS = {
    "IBMPlexSerif-SemiBold.ttf": ("Serif", "IBMPlexSerif-SemiBold.ttf"),
    "IBMPlexMono-Regular.ttf": ("Mono", "IBMPlexMono-Regular.ttf"),
}
CACHE = Path.home() / ".cache" / "ogfonts"


def font_path(name: str) -> Path:
    """Return a local path to the font, downloading it once if needed."""
    CACHE.mkdir(parents=True, exist_ok=True)
    dest = CACHE / name
    if not dest.exists():
        fam, file = FONTS[name]
        url = FONT_BASE.format(fam=fam, file=file)
        print(f"downloading {name}")
        with urlopen(url, timeout=30) as resp:
            dest.write_bytes(resp.read())
    return dest


def main() -> None:
    serif = ImageFont.truetype(str(font_path("IBMPlexSerif-SemiBold.ttf")), TAGLINE_SIZE)
    mono = ImageFont.truetype(str(font_path("IBMPlexMono-Regular.ttf")), NAME_SIZE)

    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    y = TAGLINE_TOP
    for line in TAGLINE:
        draw.text((MARGIN_X, y), line, font=serif, fill=INK)
        y += TAGLINE_LEADING

    draw.text((MARGIN_X, NAME_TOP), NAME, font=mono, fill=NAME_INK)

    out = Path(__file__).resolve().parent.parent / "static" / "og-default.png"
    img.save(out, "PNG", optimize=True)
    print(f"wrote {out} ({out.stat().st_size / 1024:.1f} KB, {WIDTH}x{HEIGHT})")


if __name__ == "__main__":
    main()
