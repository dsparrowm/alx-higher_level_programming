#!/usr/bin/python3
"""This module writes a json object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """converts a python oject to a json representation
    and writes it to a file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
