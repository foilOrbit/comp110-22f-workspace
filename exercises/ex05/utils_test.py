"""Tests the functions in utils."""

__author__ = "730548982"

from exercises.ex05.utils import only_evens, concat, sub

def test_only_evens_empty() -> None:
    """This function checks if only_evens works with an empty list."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_only_evens_odds() -> None:
    """This function checks if only_evens works with odd numbers."""
    test_list: list[int] = [1, 5, 3]
    assert only_evens(test_list) == []


def test_only_evens_evens() -> None:
    """This function checks if only_evens works with even numbers."""
    test_list: list[int] = [4, 4, 4]
    assert only_evens(test_list) == [4, 4, 4]


def test_concat_empty() -> None:
    """This function checks if concat works with two empty lists."""
    test_list_one: list[int] = []
    test_list_two: list[int] = []
    assert concat(test_list_one, test_list_two) == []


def test_concat_same_length() -> None:
    """This function checks if concat works with lists of the same length."""
    test_list_one: list[int] = [1, 2, 3]
    test_list_two: list[int] = [4, 5, 6]
    assert concat(test_list_one, test_list_two) == [1, 2, 3, 4, 5, 6]


def test_concat_diff_length() -> None:
    """This function checks if concat works with lists of different lengths."""
    test_list_one: list[int] = [1, 2, 3, 4, 5]
    test_list_two: list[int] = [6]
    assert concat(test_list_one, test_list_two) == [1, 2, 3, 4, 5, 6]


def test_sub_empty() -> None:
    """This function checks if sub works with an empty list."""
    test_list: list[int] = []
    assert sub(test_list, 1, 3) == []


def test_sub_output_one() -> None:
    """This function checks if sub works with two indexes one unit apart."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert sub(test_list, 1, 2) == [2]


def test_sub_output_multi() -> None:
    """This function checks if sub works with two indexes multiple units apart."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert sub(test_list, 0, 5) == [1, 2, 3, 4, 5]