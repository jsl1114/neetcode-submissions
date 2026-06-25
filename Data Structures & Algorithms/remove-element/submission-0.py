class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        return [i for i in nums if i != val]