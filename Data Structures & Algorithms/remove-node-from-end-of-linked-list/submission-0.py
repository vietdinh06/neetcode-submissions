# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        l = dummy
        r = dummy

        for gap in range(n + 1):
            r = r.next

        while r:
            r = r.next
            l = l.next


        prev_n = l
        next_n = l.next.next

        prev_n.next = next_n

        return dummy.next

        
            
        