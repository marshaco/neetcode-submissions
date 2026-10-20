# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.diameter = 0

        def maxDepth(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            leftDepth = maxDepth(root.left)
            rightDepth = maxDepth(root.right)
            self.diameter = max(self.diameter, leftDepth + rightDepth)

            return max(maxDepth(root.left)+1, maxDepth(root.right)+1)

        maxDepth(root)

        return self.diameter