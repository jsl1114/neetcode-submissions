class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            min_h_index = l if heights[l] < heights[r] else r
            cur_area = min(heights[l], heights[r]) * (r-l)
            max_area = max_area if cur_area < max_area else cur_area
            
            if min_h_index == l:
                l += 1
            else:
                r -= 1
        
        return max_area
            
