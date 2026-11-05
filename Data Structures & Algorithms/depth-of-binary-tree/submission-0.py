# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthHelper(root)


    def maxDepthHelper(self, root):
        if not root:
            return 0

        left = self.maxDepthHelper(root.left)
        right = self.maxDepthHelper(root.right)

        return 1 + max(left, right)