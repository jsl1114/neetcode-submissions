class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        if len(nums) == 2: return nums[0] >= 1
        goal = len(nums) - 2
        curIdx = goal - 1

        while curIdx >= 0:
            if (nums[curIdx] + curIdx == goal):
                goal = curIdx
                if goal == 0:
                    break
                curIdx = goal - 1
            else:
                curIdx -= 1
        
        return goal == 0
