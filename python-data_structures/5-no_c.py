#!/usr/bin/python3
"""Defines a function that removes all 'c' and 'C' characters from a string."""


def no_c(my_string):
    """Return a new string with all 'c' and 'C' characters removed."""
    return ''.join([char for char in my_string if char != 'c' and char != 'C'])

