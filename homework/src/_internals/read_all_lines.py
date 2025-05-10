import os


def read_all_lines(input_folder):

    Lines = []
    for filname in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filname)
        with open(file_path, "r", encoding="utf-8") as f:
            Lines.extend(f.readlines())
    return Lines
