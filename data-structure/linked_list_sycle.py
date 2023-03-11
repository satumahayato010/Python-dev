from __future__ import annotations
from typing import List, Any, Optional


class ListNode:
    def __init__(self, data: Any, next_node: ListNode) -> None:
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
    head = [3, 2, 0, -4]
    solution = Solution()
    solution.has_cycle(head)
