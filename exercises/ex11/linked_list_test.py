"""Tests for linked list utils."""


import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730548982"


def test_last_empty() -> None:
    """Last of an empty linked list should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should resturn its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Empty linked list raises index error."""
    with pytest.raises(IndexError):
        value_at(None, 1)


def test_value_at_non_empty() -> None:
    """Return data at index."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 2) == 3


def test_max_empty() -> None:
    """Empty list returns None."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty() -> None:
    """Return max value in linked list."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert max(linked_list) == 3


def test_linkify_empty() -> None:
    """Empty list returns None."""
    assert linkify([]) == None


def test_linkify_non_empty() -> None:
    """Return linked list."""
    linked_list = Node(1, Node(2, Node(3, None)))

    assert linkify([1, 2, 3]) == linked_list


def test_scale_empty() -> None:
    """Empty list returns None."""
    assert scale(None, 1) == None


def test_scale_non_empty() -> None:
    """Return scaled linked list."""
    linked_list = Node(1, Node(2, Node(3, None)))
    print(scale(linked_list, 2))
    assert scale(linked_list, 2) == Node(2, Node(4, Node(6, None)))