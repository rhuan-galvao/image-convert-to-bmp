from PIL import Image
import os

# List all files in path
actual_path = os.getcwd()
dir_list = os.listdir(actual_path)

while True:
  command = input(">> ").strip()

  if command.lower == "exit":
    break
  elif command == "list":
    print(dir_list)
  elif command == "convert":
    input_img = input("Type your filename to convert: ")

    try:
      with Image.open(input_img) as img:
        img.verify()
        print("Format", img.format)

        def convert_bmp(input_path, output_path=None):
          image = Image.open(input_path)
          image = image.convert("RGB")

          if not output_path:
            output_path = os.path.splitext(input_path)[0] + ".bmp"

            image.save(output_path, "BMP")

            print(f'Converted: {input_path} to {output_path}')

        convert_bmp(input_img)
    except:
      print("Invalid")
  else:
    print("Invalid command")