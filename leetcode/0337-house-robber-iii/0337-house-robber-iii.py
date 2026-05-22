class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dfs(node):
            if not node:
                return 0
            if node in memo:
                return memo[node]
            rob_this = node.val
            if node.left:
                rob_this += dfs(node.left.left)
                rob_this += dfs(node.left.right)
            if node.right:
                rob_this += dfs(node.right.left)
                rob_this += dfs(node.right.right)
            skip_this = dfs(node.left) + dfs(node.right)
            memo[node] = max(rob_this, skip_this)
            return memo[node]
        return dfs(root)