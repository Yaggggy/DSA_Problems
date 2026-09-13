# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,lval,rval):
        if not root: return True
        if root.val <= lval or root.val >= rval: return False
        return self.dfs(root.left,lval,root.val) and self.dfs(root.right,root.val,rval)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root,float("-inf"),float("inf"))