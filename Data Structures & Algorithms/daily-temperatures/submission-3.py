class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [(0,temperatures[0])]

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                    li, _ = stack.pop()
                    res[li] = i - li
            stack.append((i, temperatures[i]))

        return res