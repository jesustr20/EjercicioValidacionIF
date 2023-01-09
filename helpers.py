import os

def whatSystem(system):
  match system:
    case "Windows":
      clean = "cls"
    case "Linux" | "Darwin" | "MacOS":
      clean = "clear"
    case _: # Default
      clean = "clear"
  return os.system(clean)