#!/usr/bin/python3
"""this module converts python objects to JSON"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    y = json.dumps(my_obj)
    return y
