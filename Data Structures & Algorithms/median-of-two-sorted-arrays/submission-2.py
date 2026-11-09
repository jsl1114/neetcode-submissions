class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        even = (len(nums1) + len(nums2)) % 2 == 0
        n = len(nums1) + len(nums2)
        res = []
        i, j = 0, 0

        while (i + j) < n // 2 + 1:
            if i < len(nums1) and (j == len(nums2) or nums1[i] < nums2[j]):
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        
        return res[-1] if not even else (res[-1] + res[-2]) / 2