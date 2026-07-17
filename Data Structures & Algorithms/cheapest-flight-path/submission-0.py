class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        adj = defaultdict(list)
        dist = [[INF] * (k + 5) for _ in range(n)]
        for u, v, cost in flights:
            adj[u].append([v, cost])
        
        dist[src][0] = 0
        minHeap = [(0, src, -1)]

        while len(minHeap):
            cost, node, stops = heapq.heappop(minHeap)
            if dst == node:
                return cost
            if stops == k or dist[node][stops + 1] < cost:
                continue
            for n, w in adj[node]:
                nextCost = cost + w
                nextStops = 1 + stops
                if dist[n][nextStops + 1] > nextCost:
                    dist[n][nextStops + 1] = nextCost
                    heapq.heappush(minHeap, (nextCost, n, nextStops))
        return -1
