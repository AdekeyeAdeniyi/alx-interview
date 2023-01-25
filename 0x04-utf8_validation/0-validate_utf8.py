#!/usr/bin/python3
"""
Validate if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    if not data and len(data) <= 0:
        return False
    result = all([True if val <= 128 else False for val in data])
    return result
