import os
import sys
import string
import random
import secrets
import argparse
import subprocess

RED = "\033[31m"
GREEN = "\033[32m"
BOLD = "\033[1m"

def id_generator(size=17, chars=string.ascii_uppercase):
    return ''.join(secrets.choice(chars) for _ in range(size))

def remove_exif_data(file_path):
    filename, extension = os.path.splitext(os.path.basename(file_path))
    new_filename = id_generator() + extension
    new_file_path = os.path.join(os.path.dirname(file_path), new_filename)
    os.rename(file_path, new_file_path)
    subprocess.call(['exiftool', '-overwrite_original', '-all=', new_file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"{BOLD}{GREEN}File {filename}{extension} has been changed to {new_filename} and exif data has been removed{BOLD}")

def remove_exif_data_recursively(dir_path):
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            remove_exif_data(file_path)
        elif os.path.isdir(file_path):
            remove_exif_data_recursively(file_path)
    subprocess.call(['exiftool', '-overwrite_original', '-all:all=', '-r', dir_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remove exif data from a file or directory recursively')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', help='Remove exif data from a file')
    group.add_argument('-d', '--directory', help='Remove exif data from a directory recursively')
    args = parser.parse_args()

    if args.file:
        file_path = args.file
        if not os.path.isfile(file_path):
            print(f"{BOLD}{RED}Please enter a valid file path{BOLD}")
            sys.exit()
        remove_exif_data(file_path)

    if args.directory:
        dir_path = args.directory
        if not os.path.isdir(dir_path):
            print(f"{BOLD}{RED}Please enter a valid directory path{BOLD}")
            sys.exit()
        remove_exif_data_recursively(dir_path)

# - Created by 0x1717 aka GYG3S