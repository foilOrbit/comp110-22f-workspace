""""""

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