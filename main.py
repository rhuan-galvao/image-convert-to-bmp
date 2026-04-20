from PIL import Image
import os

def convert_to_bmp(input_path, output_path=None):
  img = Image.open(input_path)

  img = img.convert("RGB")

  if not output_path:
    output_path = os.path.splitext(input_path)[0] + ".bmp"

  img.save(output_path, "BMP")

  print(f'Convetido: {input_path} para {output_path}')


convert_to_bmp("test_image.jpg")
