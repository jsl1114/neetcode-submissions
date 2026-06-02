class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def kadanes(arr):
            maxSum = nums[0]
            curSum = 0

            for num in arr:
                curSum = max(0, curSum)
                curSum += num
                maxSum = max(maxSum, curSum)
            
            return maxSum

        return kadanes(nums)
