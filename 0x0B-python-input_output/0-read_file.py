#!/usr/bin/python3
"""Reads a text file and prints it to stdout"""


def read_file(filename=""):
    """reads a text file(utf8) and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
        f.close()
