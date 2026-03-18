class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
        return res