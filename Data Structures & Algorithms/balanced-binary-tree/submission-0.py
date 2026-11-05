# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, height = self.isBalancedHelper(root)
        return balanced
    
    def isBalancedHelper(self, root, ):
        if not root:
            return (True, 0)

        leftB, leftHeight = self.isBalancedHelper(root.left)
        rightB, rightHeight = self.isBalancedHelper(root.right)

        balanced = (leftB and rightB and (abs(leftHeight - rightHeight)) <= 1)
        height = 1 + max(leftHeight, rightHeight)

        return (balanced, height)