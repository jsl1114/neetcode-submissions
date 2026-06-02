from collections import defaultdict

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            p, pivot = l, nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = pivot, nums[p]

            if p < k:
                return quickSelect(p+1, r)
            elif p > k:
                return quickSelect(l, p-1)
            return pivot

        return quickSelect(0, len(nums) - 1)