#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    """a function that replaces an element of a list at a specific position"""
    if not (idx < 0 or idx >= len(my_list)):
        my_list[idx] = element
    return my_list
