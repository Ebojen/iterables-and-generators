from linked_list_iterator import LinkedListIterable
from linked_list_generator import LinkedListGenerator as GeneratorLinkedList


def main():
    print("Working with a linked list that uses an explicit iterator class:")
    linked_list = LinkedListIterable[int]()
    linked_list.add_item(1).add_item(2).add_item(3)
    print(linked_list)

    for node in linked_list:
        print(node.data)

    print("\nWorking with a linked list that uses a generator-based iterator:")
    generator_linked_list = GeneratorLinkedList[int]()
    generator_linked_list.add_item(4).add_item(5).add_item(6)
    print(generator_linked_list)

    for node in generator_linked_list:
        print(node.data)


if __name__ == "__main__":
    main()
