class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = [0] * numCourses
        outd = defaultdict(list)

        for c, p in prerequisites:
            ind[c] += 1
            outd[p].append(c)
        
        q = deque()
        for n in range(numCourses):
            if ind[n] == 0:
                q.append(n)
        
        finished = 0
        while q:
            node = q.popleft()
            finished += 1
            for n in outd[node]:
                ind[n] -= 1
                if ind[n] == 0:
                    q.append(n)
        
        return finished == numCourses
        
