class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(state):
            if len(state) == len(nums):
                res.append(state[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in state:
                    continue
                state.append(nums[i])
                dfs(state)
                state.pop(-1)
        
        dfs([])
        
        return res