# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        lis = set()
        def help(node):
            if not node:
                return False
            rem = k - node.val
            if rem in lis:
                return True
            lis.add(node.val)
            l = help(node.left)
            r = help(node.right)
            return l or r
        return help(root)

