"""This program performs three unit tests for each function."""

__author__ = "730548982"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """This will test if the function works with an empty dictionary."""
    assert invert({}) == {}


def test_invert_multiple() -> None:
    """This will test if the function works with a dictionary with multiple entries and no duplicate values."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_single() -> None:
    """This will test if the function works with a dictionary with one entry."""
    assert invert({"Kris": "Jordan"}) == {"Jordan": "Kris"}


# Test favorite_color
def test_favorite_color_empty() -> None:
    """This will test if the function works with an empty dictionary."""
    assert favorite_color({}) == ""


def test_favorite_color_multiple() -> None:
    """This will test if the function works with a dictionary with multiple entries and no duplicate values."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_order() -> None:
    """This will test if the function works with a dictionary with one entry."""
    assert favorite_color({"Kris": "blue", "Ezri": "blue", "Marc": "yellow", "George": "yellow"}) == "blue"


# Test count
def test_count_empty() -> None:
    """This will test if the function works with an empty dictionary."""
    assert count({}) == {}


def test_count_multiple() -> None:
    """This will test if the function works with a dictionary with multiple entries and no duplicate values."""
    assert count(["yellow", "blue", "blue"]) == {"yellow": 1, "blue": 2}


def test_count_single() -> None:
    """This will test if the function works with a dictionary with one entry."""
    assert count(["yellow"]) == {"yellow": 1}