# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        visited = {}
        stack1 = [p]
        stack2 = [q]
    
        # Both are None
        # Left is None
        # Right is None
        # Both have values

        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()

            if node1 and node2:
                if node1.val == node2.val:
                    stack1.append(node1.right)
                    stack1.append(node1.left)

                    stack2.append(node2.right)
                    stack2.append(node2.left)
                else:
                    return False
            else:
                if not node1 and not node2:
                    continue
                else:
                    return False
        return True
            

