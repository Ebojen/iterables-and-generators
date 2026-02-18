import pytest

from linked_list_iterator import LinkedListIterable


def test_linked_list_add_and_iteration():
    ll = LinkedListIterable[int]()
    ll.add_item(1).add_item(2).add_item(3)

    collected = [node.data for node in ll]
    assert collected == [1, 2, 3]


def test_iterator_returns_nodes_and_is_independent():
    ll = LinkedListIterable[int]()
    ll.add_item(10).add_item(20)

    it1 = iter(ll)
    it2 = iter(ll)

    n1 = next(it1)
    n2 = next(it2)
    assert n1.data == 10
    assert n2.data == 10

    # advance first iterator and ensure second still yields the next item
    n1_next = next(it1)
    assert n1_next.data == 20
    n2_next = next(it2)
    assert n2_next.data == 20

    with pytest.raises(StopIteration):
        next(it1)
