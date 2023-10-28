#!/usr/bin/python3
"""
From JSON string to Object module
"""
import json


def from_json_string(my_str):
    """
    function that returns an object
    represented by JSON string
    """
    return json.loads(my_str)
