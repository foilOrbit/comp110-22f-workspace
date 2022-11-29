"""Utility functions for working with Linked Lists."""


from __future__ import annotations
from typing import Optional


__author__ = "730548982"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for second argument."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"

    
def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (Values and order) equal."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else: 
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a linked list or raises a ValueError."""
    if head is None:
        raise ValueError("last cannot be called with None")
    elif head.next is None:
        return head.data
    else:
        return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns data of Node stored at the given index or raises a ValueError if the index does not exist."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.data
    else: 
        if head.next == None:
            raise IndexError("Index is out of bounds on the list.")
        else:
            return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Returns max data value in linked list or raises ValueError if empty."""
    if head is None:
        raise ValueError("Cannot call max with None.")

    if head.next == None:
        return head.data

    counter: int = max(head.next)
    if counter > head.data:
        return counter
    else:
        return head.data 
        

def linkify(items: list[int]) -> Optional[Node]:
    """Turns int list into linked list of Nodes."""
    if len(items) == 0:
        return None

    head: Node = Node(items[0], None)
    head.next = linkify(items[1:])
    print(head)
    return head


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Scales linked list based on factors."""
    if head is None:
        return None
    
    new: Node = Node(head.data * factor, None)
    new.next = scale(head.next, factor)

    return new

    