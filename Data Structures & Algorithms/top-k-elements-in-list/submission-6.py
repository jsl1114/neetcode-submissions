class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in sorted(list(Counter(nums).items()), key=lambda x: x[1], reverse=True)[:k]]