# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def lowestCommonAncestorHelper(root, p, q):
            if not root:
                return

            if root.val > p.val and root.val > q.val:
                return lowestCommonAncestorHelper(root.left, p, q)

            elif root.val < p.val and root.val < q.val:
                return lowestCommonAncestorHelper(root.right, p, q)

            else:
                return root

        return lowestCommonAncestorHelper(root, p, q)