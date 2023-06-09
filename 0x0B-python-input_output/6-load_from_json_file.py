#!/usr/bin/python3
"""
Module for function: load_from_json_file
"""

import json


def load_from_json_file(filename):
    """
    function tht creates an Objects from a "JSON file"
    """
    with open(filename, 'r', encoding='utf-8') as fi_le:
        return json.load(fi_le)
