from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values: List[int]) -> Optional[ListNode]:
    """Convert Python list -> Linked List"""
    dummy = ListNode()
    current = dummy

    for v in values:
        current.next = ListNode(v)
        current = current.next

    return dummy.next


def print_list(head: Optional[ListNode]) -> None:
    """Print linked list nicely"""
    current = head
    result = []
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result) if result else "Empty")


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next


list1 = build_list([1, 3, 5])
list2 = build_list([2, 4, 6])
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)
print_list(merged_list)
