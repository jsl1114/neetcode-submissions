class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for n in nums:
            dic[n] += 1
        
        return [item[0] for item in sorted(dic.items(),key=lambda x: x[1], reverse=True)[:k]]