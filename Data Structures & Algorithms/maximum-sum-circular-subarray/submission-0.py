class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gMax, gMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = sum(nums)

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            gMax = max(gMax, curMax)
            gMin = min(gMin, curMin)
        
        return max(gMax, total - gMin) if gMax > 0 else gMax