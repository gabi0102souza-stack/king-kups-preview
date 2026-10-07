"""Create responsive WebP copies of the three documented real photographs.

Requires Pillow. Source files are kept in ignored .asset-originals/.
Only orientation, resizing and re-encoding are performed.
"""
from pathlib import Path
from PIL import Image, ImageOps

root = Path(__file__).resolve().parents[1]
for name, widths in {
    'food': (480, 800, 960),
    'truck': (600, 1000, 1365),
    'wonton': (480, 800, 960),
}.items():
    with Image.open(root / '.asset-originals' / f'{name}.jpg') as source:
        image = ImageOps.exif_transpose(source).convert('RGB')
        for width in widths:
            copy = image.copy()
            copy.thumbnail((width, round(image.height * width / image.width)), Image.Resampling.LANCZOS)
            output = root / 'assets' / f'{name}-{width}.webp'
            copy.save(output, 'WEBP', quality=83, method=6)
            print(f'{output.name}: {copy.width}x{copy.height}, {output.stat().st_size:,} bytes')
