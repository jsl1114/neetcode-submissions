class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start, targetLeft, path):
            if targetLeft == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(nums)):
                if nums[i] > targetLeft:
                    return
                path.append(nums[i])
                backtrack(i, targetLeft - nums[i], path)
                path.pop()
                

        backtrack(0, target, [])
        return res