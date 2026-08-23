class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = defaultdict(int)
        outd = defaultdict(list)
        q = deque()
        completed = 0

        for c, p in prerequisites:
            ind[c] += 1
            outd[p].append(c)
        
        for c in range(numCourses):
            if ind[c] == 0:
                q.append(c)
        
        while q:
            curCourse = q.popleft()
            completed += 1
            for other in outd[curCourse]:
                ind[other] -= 1
                if ind[other] == 0:
                    q.append(other)
        
        return completed == numCourses