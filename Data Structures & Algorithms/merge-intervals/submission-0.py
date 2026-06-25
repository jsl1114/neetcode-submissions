class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        cur = 0
        start, end = 0, 0
        res = []

        for s, e in intervals:
            dic[s] += 1
            dic[e] -= 1
        
        for k in sorted(dic):
            cur += dic[k]
            if cur > 0 and dic[k] > 0:
                start = k
            if cur == 0:
                res.append([start, k])
        
        return res