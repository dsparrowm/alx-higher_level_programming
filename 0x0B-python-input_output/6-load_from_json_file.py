#!/usr/bin/python3
"""creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates an object from a json file"""
    witn open(filename, "r") as f:
    return json.load(f)
