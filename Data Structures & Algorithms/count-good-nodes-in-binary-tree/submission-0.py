# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret = [0]

        def dfs(node, curPathMax):
            if not node:
                return
            if node.val >= curPathMax:
                curPathMax = node.val
                ret[0] += 1
            dfs(node.left, curPathMax)
            dfs(node.right, curPathMax)
        
        dfs(root, -float('inf'))

        return ret[0]
            