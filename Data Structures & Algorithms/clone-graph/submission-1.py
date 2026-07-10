"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        ret = {}

        def dfs(node):
            if node in ret:
                return ret[node]
            
            cp = Node(node.val)
            ret[node] = cp
            for n in node.neighbors:
                cp.neighbors.append(dfs(n))
            return cp

        return dfs(node) if node else None