class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify_max(nums)
        self.nums = nums

    def add(self, val: int) -> int:
        heapq.heappush_max(self.nums, val)
        return heapq.nlargest(self.k, self.nums)[-1]