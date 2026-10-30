# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half_head = slow.next
        slow.next = None

        second_half_next = second_half_head.next
        second_half_head.next = None

        while (second_half_next):
            second_half_next_next = second_half_next.next
            second_half_next.next = second_half_head
            second_half_head = second_half_next
            second_half_next = second_half_next_next

        first_head = head
        second_head = second_half_head

        while first_head and second_head:
            first_head_next = first_head.next
            first_head.next = second_head

            second_head_next = second_head.next
            second_head.next = first_head_next
            
            second_head = second_head_next
            first_head = first_head_next




