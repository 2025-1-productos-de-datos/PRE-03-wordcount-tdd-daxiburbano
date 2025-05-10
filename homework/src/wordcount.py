# Ejemplo del caso de uso:
# python3 -m homework --input data/input data/output

# import argparse
# import sys


# def parse_args():
#     parser = argparse.ArgumentParser(description="count woerds in files")
#     parser.add_argument(
#         "input_folder", help="Path to the input folder containing files to process"
#     )
#     parser.add_argument(
#         "output_folder",
#         help="Path to the output folder for results",
#     )

#     parsed_args = parser.parse_args()

#     return parsed_args.input, parsed_args.output


# def main():
#     input_folder, output_folder = parse_args()  # entrega carpeta de entrada y salida
#     print("input folder:", input_folder)
#     print("output folder:", output_folder)


import argparse
import os
import sys


def parse_args():

    parser = argparse.ArgumentParser(description="Count words in files.")
    parser.add_argument(
        "input",
        type=str,
        help="Path to the input folder containing files to process",
    )
    parser.add_argument(
        "output",
        type=str,
        help="Path to the output folder for results",
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output


def read_all_lines(input_folder):

    Lines = []
    for filname in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filname)
        with open(file_path, "r", encoding="utf-8") as f:
            Lines.extend(f.readlines())
    return Lines


def main():
    input_folder, output_folder = parse_args()
    lines = read_all_lines(input_folder)

    # print("input foder:", input_folder)
    # print("output folder:", output_folder)
