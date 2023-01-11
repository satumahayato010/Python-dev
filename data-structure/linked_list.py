from __future__ import annotations


class Node(object):
    def __init__(self, data: int, next_node: Node = None) -> None:
        self.data = data
        self.next = next_node


class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data: int):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data: int) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data: int) -> None:
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def reverse_iterative(self) -> None:
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: Node, previous_node: Node):
            if not current_node:
                return previous_node

            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, previous_node)

        self.head = _reverse_recursive(self.head, None)


if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.print()
    print("#################")
    l.reverse_recursive()
    l.print()
