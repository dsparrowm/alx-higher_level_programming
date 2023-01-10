#!/usr/bin/python3
"""Thos module appends text to the end of the file"""


def append_write(filename="", text=""):
    """appends text to the file"""
    with open(filename, "a", encoding="utf-8") as f:
        file_no = f.write(text)
    return file_no
