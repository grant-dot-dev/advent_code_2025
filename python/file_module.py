import os

def loadFile(is_dev:bool):
    base = os.path.dirname(__file__)
    filename = "example.txt" if is_dev else "input.txt"
    file_path = os.path.join(base, filename)

    return file_path