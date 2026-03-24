# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        mapp = {num:i for i, num in enumerate(postorder)}
        def dfs(i1, i2, j1, j2):
            if i1 > i2 or j1 > j2:
                return None
            root = TreeNode(preorder[i1])
            if i1 != i2:
                left = preorder[i1+1]
                mid = mapp[left]
                size = mid - j1 + 1
                root.left = dfs(i1+1, i1+size, j1, mid)
                root.right = dfs(i1+size+1, i2, mid+1, j2-1)
            return root
        return dfs(0, n-1, 0, n-1)