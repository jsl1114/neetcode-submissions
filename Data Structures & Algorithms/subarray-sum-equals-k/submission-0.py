class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = {0:1}
        res = curSum = 0

        for num in nums:
            curSum += num
            diff = curSum - k
            res += hmap.get(diff, 0)
            hmap[curSum] = hmap.get(curSum, 0) + 1

        return res 
