# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        dummy = ListNode()
        dummy_head = dummy

        while l1 and l2:
            val = l1.val + l2.val + carry
            digit = val % 10

            if val == 0:
                carry = 0
            else:
                carry = val // 10

            dummy_head.next = ListNode(digit, None)
            dummy_head = dummy_head.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + carry
            digit = val % 10
            if val == 0:
                carry = 0
            else:
                carry = val // 10
            dummy_head.next = ListNode(digit, None)
            dummy_head = dummy_head.next
            l1 = l1.next
        
        while l2:
            val = l2.val + carry
            digit = val % 10
            if val == 0:
                carry = 0
            else:
                carry = val // 10
            dummy_head.next = ListNode(digit, None)
            dummy_head = dummy_head.next
            l2 = l2.next

        if l1 is None and l2 is None and carry:
            dummy_head.next = ListNode(carry, None)


        return dummy.next
            