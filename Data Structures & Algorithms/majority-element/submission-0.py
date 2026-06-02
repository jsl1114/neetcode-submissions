class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for num in nums:
            res[num] = res.get(num, 0) + 1
        return max(res, key=res.get)