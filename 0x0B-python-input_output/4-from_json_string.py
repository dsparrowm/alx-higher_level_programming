#!/usr/bin/python3
"""This module converts a JSON string to a python object"""
import json


def from_json_string(my_str):
    """returns a python object from a json representation"""
    return (json.loads(my_str))
