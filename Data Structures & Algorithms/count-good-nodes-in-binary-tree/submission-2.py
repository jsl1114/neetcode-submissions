# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret = 0

        def dfs(node,maxSoFar):
            nonlocal ret
            if not node:
                return
            
            if node.val >= maxSoFar:
                ret += 1
            
            maxSoFar = max(node.val, maxSoFar)
            dfs(node.left, maxSoFar)
            dfs(node.right, maxSoFar)

        dfs(root, -float("inf"))
        return ret