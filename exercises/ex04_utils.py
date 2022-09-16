"""This program will make a series of lists."""

__author__ = "730548982"


def all(given_list: list[int], given_number: int) -> bool:
    """This function compares a list's values to a given number and returns true if they match."""
    i: int = 0
    if len(given_list) == 0:
        return False
    while i < len(given_list):
        if given_list[i] != given_number:
            return False
        i += 1
    return True


def max(given_list: list[int]) -> int:
    """This function returns the largest number in a given list."""
    if len(given_list) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max_number: int = given_list[i]
    while i < len(given_list):
        if max_number < given_list[i]:
            max_number = given_list[i]
        i += 1
    return max_number


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """This function determines if two lists have deep equality."""
    i: int = 0
    if len(list_one) != len(list_two):
        return False
    while i < len(list_one) and i < len(list_two):
        if list_one[i] != list_two[i]:
            return False
        i += 1
    return True