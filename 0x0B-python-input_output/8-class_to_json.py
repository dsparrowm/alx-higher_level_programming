#!/usr/bin/python3
"""This module returns a dictionary desc kf simple data structure"""


def class_to_json(obj):
    """function that returns the dict desc with simple data"""
    return obj.__dict__
