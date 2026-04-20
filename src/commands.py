import os
from src.image_service import convert_to_bmp, resize_image
from src.validators import is_valid_image

def handle_command(command):
    cmd = command.lower()

    if cmd == "help":
        print("Available commands: help, list, convert, resize, exit")

    elif cmd == "list":
        for file in os.listdir():
            print(file)

    elif cmd == "convert":
        file_name = input("Enter file name: ").strip()

        if not is_valid_image(file_name):
            print("Invalid image!")
            return

        convert_to_bmp(file_name)

    elif cmd == "resize":
        file_name = input("Enter file name: ").strip()

        if not is_valid_image(file_name):
            print("Invalid image!")
            return

        width = int(input("Width: "))
        height = int(input("Height: "))

        resize_image(file_name, width, height)

    else:
        print("Unknown command")