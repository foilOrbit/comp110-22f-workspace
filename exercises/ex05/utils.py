"""This program contains three functions to modify lists."""

__author__ = "730548982"


def only_evens(input_list: list[int]) -> list[int]:
    """This function returns the even numbers in a list."""
    output_list: list[int] = []
    i: int = 0
    while i < len(input_list):
        if input_list[i] % 2 == 0:
            output_list.append(input_list[i])
            i += 1
        else:
            i += 1
    return output_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """This function concatenates list_two to the end of list_one."""
    output_list: list[int] = []
    i: int = 0
    while i < len(list_one):
        output_list.append(list_one[i])
        i += 1
    i = 0
    while i < len(list_two):
        output_list.append(list_two[i])
        i += 1
    return output_list


def sub(input_list: list[int], start: int, end: int) -> list[int]:
    """This function creates a subset list beginning at start and finishing at end - 1."""
    output_list: list[int] = []
    i: int = start
    if start < 0:
        i = 0
    while i < end and i < len(input_list):
        output_list.append(input_list[i])
        i += 1
    return output_list