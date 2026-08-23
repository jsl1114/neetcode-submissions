class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(i, tot):
            if i == len(nums):
                return tot == target
            
            return (backtrack(i + 1, tot + nums[i]) + backtrack(i + 1, tot - nums[i]))
        
        return backtrack(0, 0)