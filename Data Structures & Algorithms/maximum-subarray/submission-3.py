class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = nums[0]
        allMax = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            curMax = max(num, curMax + num)
            allMax = max(allMax, curMax)

        return allMax