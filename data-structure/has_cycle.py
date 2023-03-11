from __future__ import annotations
from typing import List, Any, Optional


class ListNode:
    def __init__(self, data: Any, next_node: ListNode = None) -> None:
        self.data = data
        self.next = next_node


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        dictionary = {}
        while head:
            if head in dictionary:
                return True
            else:
                dictionary[head] = True
            head = head.next
        return False


if __name__ == '__main__':
    head = ListNode(3)
    node1 = ListNode(2)
    node2 = ListNode(0)
    node3 = ListNode(-4)

    head.next = node1
    node1.next = node2
    node2.next = node3

    solution = Solution()
    print(solution.has_cycle(head))
