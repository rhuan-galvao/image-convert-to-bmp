from PIL import Image
import os

def convert_to_bmp(input_path, output_path=None):
    with Image.open(input_path) as image:
        has_alpha = image.mode in ("RGBA", "LA") or "transparency" in image.info

        if not output_path:
            output_path = os.path.splitext(input_path)[0] + ".bmp"

        if has_alpha:
            # BMP não mantém transparência real.
            # Aqui você pode decidir fundo transparente em PNG ou aplicar fundo sólido.
            image = image.convert("RGBA")
            background = Image.new("RGBA", image.size, (0, 0, 0, 0))
            image = Image.alpha_composite(background, image).convert("RGB")
        else:
            image = image.convert("RGB")

        image.save(output_path, "BMP")
        print(f"Converted: {input_path} -> {output_path}")


def resize_image(input_path, width, height, output_path=None):
    with Image.open(input_path) as image:
        resized = image.resize((width, height))

        if not output_path:
            name, ext = os.path.splitext(input_path)
            output_path = f"{name}_{width}x{height}{ext}"

        resized.save(output_path)
        print(f"Resized: {input_path} -> {output_path}")