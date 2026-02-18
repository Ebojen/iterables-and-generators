import pytest

from node import Node


def test_node_pointer_accepts_same_type():
    n1 = Node[int](1)
    n2 = Node[int](2)
    n1.pointer = n2
    assert n1.pointer is n2


def test_node_pointer_rejects_none():
    n = Node[int](1)
    with pytest.raises(ValueError):
        n.pointer = None  # type: ignore


def test_node_pointer_rejects_non_node():
    n = Node[int](1)
    with pytest.raises(TypeError):
        n.pointer = 5  # type: ignore


def test_node_pointer_rejects_type_mismatch():
    n_int = Node[int](1)
    n_str = Node[str]("a")
    with pytest.raises(TypeError):
        n_int.pointer = n_str  # type: ignore
