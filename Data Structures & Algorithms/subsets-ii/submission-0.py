class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, state):
            if i == len(nums):
                res.append(state[:])
                return

            state.append(nums[i])
            dfs(i+1, state)
            state.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            dfs(i + 1, state)
        
        dfs(0,[])
        return res