# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashed = set()

        cur_head = head

        while cur_head is not None:
            if cur_head in hashed:
                return True
            else:
                hashed.add(cur_head)
            cur_head = cur_head.next
            
        return False