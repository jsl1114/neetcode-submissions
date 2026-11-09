# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = 0

        def dfs(node):
            nonlocal ret

            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)

            ret = max(ret, l + r)

            return max(l, r) + 1
        
        dfs(root)
        return ret