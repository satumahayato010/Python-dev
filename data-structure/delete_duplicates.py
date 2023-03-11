from __future__ import annotations
from typing import Optional, Any


class ListNode:
    def __init__(self, data: Any, next_node: ListNode = None) -> None:
        self.data = data
        self.next = next_node


class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev_node = head
        current_node = head.next

        while current_node:
            if current_node.data == prev_node.data:
                prev_node.next = current_node.next
                current_node = current_node.next
            else:
                prev_node = current_node
                current_node = current_node.next

        return head

    def delete_duplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        current = head
        prev = dummy
        while current and current.next:
            while current.next and current.data == current.next.data:
                current = current.next
            if prev.next == current:
                prev = prev.next
            else:
                prev.next = current.next

            current = current.next

        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(4)
    node6 = ListNode(5)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    solution = Solution()
    node = solution.delete_duplicates2(head)

    while node:
        print(node.data)
        node = node.next
