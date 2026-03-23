# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        def dfs(node, maxi, mini):
            if not node:
                return maxi - mini
            maxi = max(maxi, node.val)
            mini = min(mini, node.val)
            left = dfs(node.left, maxi, mini)
            right = dfs(node.right, maxi, mini)
            return max(left, right)
        return dfs(root, root.val, root.val)

                
