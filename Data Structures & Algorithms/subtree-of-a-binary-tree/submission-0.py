# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSubtreeHelper(root, subroot):
            def isSameTreeHelper(p, q):
                if not p and not q:
                    return True

                if not p or not q:
                    return False

                if p.val != q.val:
                    return False

                left = isSameTreeHelper(p.left, q.left)
                right = isSameTreeHelper(p.right, q.right)

                return left and right

            if not root:
                return False

            status = isSameTreeHelper(root, subroot)

            if status:
                return True

            left = isSubtreeHelper(root.left, subroot)
            right = isSubtreeHelper(root.right, subroot)

            return left or right

        return isSubtreeHelper(root, subRoot)

