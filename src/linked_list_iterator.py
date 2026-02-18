from typing import TypeVar, Generic, Optional
from node import Node


T = TypeVar("T")


class LinkedListIterator(Generic[T]):
    def __init__(self, head: Optional[Node[T]]):
        self._current_node = head

    def __iter__(self) -> "LinkedListIterator[T]":
        return self

    def __next__(self) -> Node[T]:
        if self._current_node is None:
            raise StopIteration
        node = self._current_node
        self._current_node = node.pointer
        return node


class LinkedListIterable(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None

    def add_item(self, data: T) -> "LinkedListIterable[T]":
        if self.head is None:
            self.head = Node(data)
            return self

        current_node = self.head
        while current_node.pointer is not None:
            current_node = current_node.pointer

        current_node.pointer = Node(data)
        return self

    def __iter__(self) -> LinkedListIterator[T]:
        return LinkedListIterator(self.head)

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current is not None:
            items.append(repr(current.data))
            current = current.pointer
        return f"{self.__class__.__name__}([{', '.join(items)}])"
