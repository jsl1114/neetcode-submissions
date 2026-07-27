class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        ind = [0] * (len(edges) + 1)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            ind[n1] += 1
            ind[n2] += 1
        
        q = deque()
        for i in range(1, len(edges) + 1):
            if ind[i] == 1:
                q.append(i)
        
        while q:
            node = q.popleft()
            ind[node] -= 1
            for n in adj[node]:
                ind[n] -= 1
                if ind[n] == 1:
                    q.append(n)
        
        for u, v in reversed(edges):
            if ind[u] == 2 and ind[v]:
                return [u, v]
        
        return []
        

