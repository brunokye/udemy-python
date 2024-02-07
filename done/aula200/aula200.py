from pathlib import Path
from PIL import Image

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / "original.jpg"
NEW_IMAGE = ROOT_FOLDER / "new.jpg"

pil_image = Image.open(ORIGINAL)
width, height = pil_image.size
exif = pil_image.info["exif"]

new_width = 640
new_height = round(height * (new_width / width))

new_imagem = pil_image.resize((new_width, new_height))
new_imagem.save(NEW_IMAGE, optimize=True, quality=70, exif=exif)
