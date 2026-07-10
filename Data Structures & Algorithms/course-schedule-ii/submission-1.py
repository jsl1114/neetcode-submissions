class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ind = defaultdict(int)
        outd = defaultdict(list)
        res = []

        for c, pre in prerequisites:
            ind[c] += 1
            outd[pre].append(c)
        
        q = deque()
        for n in range(numCourses):
            if ind[n] == 0:
                q.append(n)
        
        finished = 0
        while q:
            node = q.popleft()
            res.append(node)
            for nei in outd[node]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)
        
        return [] if len(res) != numCourses else res