# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, depth, mapp):
            if node:
                mapp[depth] = node.val
                if depth-2 in mapp:
                    if mapp[depth-2] % 2 == 0:
                        self.ans += node.val
            if node.left:
                dfs(node.left, depth+1, mapp)
            if node.right:
                dfs(node.right, depth+1, mapp)
        dfs(root, 1, {})
        return self.ans
            
