# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curNode = root

        while curNode:
            curVal = curNode.val

            if curVal > p.val and curVal > q.val:
                curNode = curNode.left
            elif curVal < p.val and curVal < q.val:
                curNode = curNode.right
            else:
                return curNode
