class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, len(nums)
        minLen = 0

        while l <= r and sum(nums[l:r]) >= target:
            minLen = r - l
            if nums[l] < nums[r-1]:
                l += 1
            else: 
                r -= 1
        
        return minLen


