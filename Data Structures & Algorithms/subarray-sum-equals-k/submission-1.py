class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = {0: 1}
        ret = 0
        curSum = 0
        
        for i in range(len(nums)): 
            curSum += nums[i]
            diff = curSum - k
            
            ret += pre.get(diff, 0)
            pre[curSum] = pre.get(curSum, 0) + 1
        
        return ret