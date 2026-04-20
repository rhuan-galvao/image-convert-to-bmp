from src.commands import handle_command

def run_console():
  print("Image Converter")
  print("Commands: help, list, conver, resize, exit")

  while True:
    command = input(">> ").strip()
    if not command:
      continue

    if command.lower() == "exit":
      print("Clossing program...")
      break

  
    handle_command(command)