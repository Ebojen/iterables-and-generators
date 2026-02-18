from typing import TypeVar, Generic, Optional, Iterator
from node import Node


T = TypeVar("T")


class LinkedListGenerator(Generic[T]):
    """Singly-linked list that yields `Node` objects using a generator-based iterator."""

    def __init__(self):
        self.head: Optional[Node[T]] = None

    def add_item(self, data: T) -> "LinkedListGenerator[T]":
        if self.head is None:
            self.head = Node(data)
            return self

        current_node = self.head
        while current_node.pointer is not None:
            current_node = current_node.pointer

        current_node.pointer = Node(data)
        return self

    def __iter__(self) -> Iterator[Node[T]]:
        """Generator-based iterator that yields `Node` instances.

        Each call to `iter()` returns a fresh generator, so multiple
        iterators are independent.
        """
        current = self.head
        while current is not None:
            yield current
            current = current.pointer

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current is not None:
            items.append(repr(current.data))
            current = current.pointer
        return f"{self.__class__.__name__}([{', '.join(items)}])"
