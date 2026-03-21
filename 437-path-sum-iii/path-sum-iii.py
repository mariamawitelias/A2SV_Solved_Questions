# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.path = 0
        self.mapp = defaultdict(int)
        self.mapp[0] = 1
        def dfs(node, curr):
            if node is None: 
                return
            curr += node.val
            self.path += self.mapp[curr - targetSum]
            self.mapp[curr] += 1
            if node.right:
                dfs(node.right, curr)
            if node.left:
                dfs(node.left, curr)
            self.mapp[curr] -= 1
        dfs(root, 0)
        return self.path
            