# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        if list1 is None and list2 is not None:
            return list2

        if list1 is not None and list2 is None:
            return list1

        r_head = list1
        b_head = list2

        result = ListNode()
        result_head = result

        while r_head is not None and b_head is not None:
            if r_head.val <= b_head.val:
                result_head.next = r_head
                r_head = r_head.next
            else:
                result_head.next = b_head
                b_head = b_head.next
            result_head = result_head.next

        if r_head is not None:
            result_head.next = r_head
        elif b_head is not None:
            result_head.next = b_head

        return result.next
        