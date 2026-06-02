class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = defaultdict(int)

        for t in tasks:
            dic[t] += 1
        
        maxf = max(dic.values())
        maxCount = 0
        for v in dic.values():
            maxCount += 1 if v == maxf else 0
        
        time = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), time)