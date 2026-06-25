class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        products = [1] * len(nums)
        products[0] = nums[0]
        for i in range(1, len(nums)):
            products[i] = max(products[i-1] * nums[i], nums[i])

        return max(products)