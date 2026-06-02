class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        cur = []
        res = []
        have = 0

        for s, e in intervals:
            dic[s] += 1
            dic[e] -= 1
        
        for k in sorted(dic):
            if not cur:
                cur.append(k)
            have += dic[k]
            if have == 0:
                cur.append(k)
                res.append(cur)
                cur = []
        return res