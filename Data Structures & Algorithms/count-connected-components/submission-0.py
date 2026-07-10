class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        seen = set()
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def bfs(node):
            q = deque([node])
            seen.add(node)
            while q:
                cur = q.popleft()
                for n in adj[cur]:
                    if n not in seen:
                        seen.add(n)
                        q.append(n)

        res = 0
        for node in range(n):
            if node not in seen:
                bfs(node)
                res += 1
        return res
