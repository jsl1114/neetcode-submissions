class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmax = curMax * num
            tmin = curMin * num
            curMax = max(tmax, tmin, num)
            curMin = max(tmax, tmin, num)
            res = max(res, curMax)
        
        return res