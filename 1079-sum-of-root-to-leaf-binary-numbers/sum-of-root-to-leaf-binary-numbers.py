# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def getDecimal(self, path):
        num = 0
        for bit in path:
            num = num * 2 + bit
        return num

    def getPath(self, root, path):
        if not root:
            return
        
        path.append(root.val)

        if not root.left and not root.right:
            self.ans += self.getDecimal(path)

        self.getPath(root.left, path)
        self.getPath(root.right, path)

        path.pop()  

    def sumRootToLeaf(self, root):
        if not root:
            return 0
        
        self.getPath(root, [])
        return self.ans