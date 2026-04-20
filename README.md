# 🖼️ Image Converter CLI

Simple Python CLI tool to convert and process images.

Supports:

* Convert `.jpg` / `.png` → `.bmp`
* Resize images (useful for Nintendo Switch bootloader)
* List files in current directory

---

## Commands

* `list` → list files in current folder
* `convert <file>` → convert image to `.bmp`
* `resize <file> <width> <height>` → resize image
* `exit` → close the program

---

## Requirements

```bash
pip install -r requirements.txt
```

---

## Usage

Run the program:

```bash
python main.py
```

### Examples

```bash
>> list
image.png
photo.jpg

>> convert image.png
Converted: image.png → image.bmp

>> resize image.png 1280 720
Resized: image.png → image_1280x720.png

>> exit
```

---

## Notes

* Only `.jpg` and `.png` are supported
* PNG transparency is **not preserved in BMP**
* BMP files are larger than original images
* Resize is recommended for specific resolutions (e.g. Switch bootloader)

---

## Project Structure

```bash
image_converter/
├── main.py
├── requirements.txt
└── src/
    ├── cli.py
    ├── commands.py
    ├── image_service.py
    └── validators.py
```

---

## Future Improvements

* `resize_switch` preset command
* `info <file>` (show image details)
* better command parsing
* batch conversion
