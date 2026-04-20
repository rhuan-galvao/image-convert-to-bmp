from PIL import Image
import os

def file_exists(path):
    return os.path.isfile(path)

def is_valid_image(path):
    if not file_exists(path):
        return False

    try:
        with Image.open(path) as img:
            img.verify()
        return True
    except:
        return False