#!/usr/bin/python3
"""This module writes to a file:
    if the file doesn't exist, it creates a new file.
    if the file exists, it overwrites the file"""


def write_file(filename="", text=""):
    """writes to a file, creating new file if it doesn't exists
        and overwrites if it exists
    """
    with open(filename, "w", encoding="utf-8") as f:
        file_no = f.write(text)
    return file_no
