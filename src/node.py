from typing import TypeVar, Generic, Optional


T = TypeVar("T")


class Node(Generic[T]):
    __slots__ = ["data", "_pointer"]

    def __init__(self, data: T):
        self.data: T = data
        self._pointer: Optional["Node[T]"] = None

    @property
    def pointer(self) -> Optional["Node[T]"]:
        return self._pointer

    @pointer.setter
    def pointer(self, node: "Node[T]") -> None:
        if node is None:
            raise ValueError("Pointer cannot be set to None")
        if not isinstance(node, Node):
            raise TypeError("Pointer must be an instance of Node")
        if not type(self.data) == type(node.data):
            raise TypeError(
                "Pointer must point to a node of the same type. "
                f"Expected type: {type(self.data)}, got: {type(node.data)}"
            )
        self._pointer = node

    def __repr__(self) -> str:
        ptr = f"Node({self._pointer.data!r})" if self._pointer is not None else "None"
        return f"Node(data={self.data!r}, pointer={ptr})"
