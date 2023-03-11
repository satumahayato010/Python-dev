from __future__ import annotations
from typing import Any, Optional


class ListNode:
    def __init__(self, data: Any, next_node: ListNode = None) -> None:
        self.data = data
        self.next = next_node


class Solution:
    def detect_cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        else:
            return None

        while head != slow:
            head, slow = head.next, slow.next
        return head

    def has_cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dictionary = {}
        while head:
            if head in dictionary:
                return head
            else:
                dictionary[head] = True
            head = head.next
        return None


if __name__ == '__main__':
    head = ListNode(3)
    node1 = ListNode(2)
    node2 = ListNode(0)
    node3 = ListNode(-4)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node1

    solution = Solution()
    result = solution.has_cycle(head)
    print(result.data)
