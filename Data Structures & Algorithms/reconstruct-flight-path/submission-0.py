class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for s, d in sorted(tickets)[::-1]:
            adj[s].append(d)
        
        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
        
        dfs("JFK")
        return res[::-1]