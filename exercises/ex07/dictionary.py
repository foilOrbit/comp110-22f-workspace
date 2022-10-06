"""This program creates three functions that interact with dictionaries."""

__author__ = "730548982"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """This function inverts the key and value of a dictionary."""
    output_dict: dict[str, str] = dict()
    test_list: list[str] = []
    for key in input_dict:
        test_list.append(input_dict[key])
        output_dict[input_dict[key]] = key
    i: int = 0
    while i < len(test_list):
        j: int = i + 1
        while j < len(test_list):
            if test_list[i] != test_list[j]:
                j += 1
            else:
                raise KeyError("Dictionary could not invert. Duplicate keys identified in output function.")
        i += 1
    return output_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """This function the most frequent favorite color in a dictionary."""
    color_dict: dict[str, int] = {}
    color_list: list[str] = []
    most_frequent: str = ""
    frequency: int = 0
    for key in input_dict:
        if key not in color_dict:
            color_dict[input_dict[key]] = 0
        color_list.append(input_dict[key])
    for key in color_dict:
        i: int = 0
        counter: int = 0
        while i < len(color_list):
            if key == color_list[i]:
                counter += 1
            i += 1
        color_dict[key] += counter
        if color_dict[key] > frequency:
            frequency = color_dict[key]
            most_frequent = key
    return most_frequent


def count(input_list: list[str]) -> dict[str, int]:
    """This function produces a dictionary with the list values as the key and their frequency as a value."""
    output_dict: dict[str, int] = dict()
    i: int = 0
    while i < len(input_list):
        if i not in output_dict:
            output_dict[input_list[i]] = 0
        i += 1
    for key in output_dict:
        i: int = 0
        counter: int = 0
        while i < len(input_list):
            if key == input_list[i]:
                counter += 1
            i += 1
        output_dict[key] += counter
    return output_dict