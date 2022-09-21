"""Tests the functions in utils."""

__author__ = "730548982"

from utils import only_evens


def test_only_evens_empty() -> None:
    """This function checks if only_evens works with an empty list."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_only_evens_odds() -> None:
    """This function checks if only_evens works with odd numbers."""
    test_list: list[int] = [1,5,3]
    assert only_evens(test_list) == []


def test_only_evens_evens() -> None:
    """This function checks if only_evens works with even numbers."""
    test_list: list[int] = [4,4,4]
    assert only_evens(test_list) == [4,4,4]

