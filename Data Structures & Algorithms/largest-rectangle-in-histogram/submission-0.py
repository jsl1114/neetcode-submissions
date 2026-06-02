class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret = 0
        stack = [] # (idx, h)

        for i, ele in enumerate(heights):
            start = i
            while stack and stack[-1][1] > ele:
                index, height = stack.pop()
                ret = max(ret, height * (i - index))
                start = index
            stack.append((start, ele))
        
        for i, ele in stack:
            ret = max(ret, ele * (len(heights) - i))
        
        return ret
    

