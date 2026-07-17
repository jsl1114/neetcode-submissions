class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = defaultdict(int)
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        size = end = 0
        for i, c in enumerate(s):
            end = max(end, lastIndex[c])
            size += 1
            if end == i:
                res.append(size)
                size = 0
        
        return res