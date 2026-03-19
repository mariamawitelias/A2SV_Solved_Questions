# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderSuccessor(self, node):
        while node.left is not None:
            node = node.left
        return node
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None 
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            succ = self.inorderSuccessor(root.right)
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)
        return root

            


            
