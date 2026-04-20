# 🖼️ Image to BMP Converter

Simple Python CLI tool to convert `.jpg` and `.png` images to `.bmp`.

## Commands

* `list` → list files in current folder
* `convert` → convert an image to `.bmp`
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

Example:

```bash
>> list
image.png
photo.jpg

>> convert
Enter file name: image.png
Converted: image.png to image.bmp

>> exit
```

---

## Notes

* Only `.jpg` and `.png` are supported
* PNG transparency will be removed
* BMP files are larger than original images
