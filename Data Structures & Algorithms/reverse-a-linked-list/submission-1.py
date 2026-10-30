# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        cur_head = head
        next_node = cur_head.next
        cur_head.next = None

        while (next_node is not None):
            next_next_node = next_node.next
            next_node.next = cur_head
            cur_head = next_node
            next_node = next_next_node


        return cur_head
        