class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm = []
        for i in nums:
            if i in hm:
                return i
            hm.append(i)