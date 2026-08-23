# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [(root, "lr")]
        ret = []

        while q:
            qLen = len(q)
            curLevel = []
            for _ in range(qLen):
                curNode = q.pop(0)
                node, direction = curNode[0], curNode[1]
                curLevel.append(node.val)
                nextDir = "rl" if direction == "lr" else "lr"
                if node.left:
                    q.append((node.left, nextDir))
                if node.right:
                    q.append((node.right, nextDir))
            if direction == "rl":
                curLevel = curLevel[::-1]
            ret.append(curLevel)
        
        return ret

                