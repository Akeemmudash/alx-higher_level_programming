#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """function that replaces an element in a list at a specific
    position without modifying the original list"""
    list_copy = my_list.copy()
    if not(idx < 0 or idx >= len(my_list)):
        list_copy[idx] = element
    return list_copy
