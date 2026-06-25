class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        curTurb = 0
        maxTurb = 1
        sign = ""

        for i in range(0, len(arr) - 1):
            if not sign:
                curTurb += 1
                maxTurb = max(maxTurb, curTurb)
                if arr[i] > arr[i + 1]:
                    sign = ">"
                elif arr[i] < arr[i + 1]:
                    sign = "<"
            elif sign == ">":
                if arr[i] >= arr[i + 1]:
                    curTurb = 1
                    maxTurb = max(maxTurb, curTurb)
                else:
                    sign = "<"
                    curTurb += 1
                    maxTurb = max(maxTurb, curTurb)
            elif sign == "<":
                if arr[i] <= arr[i + 1]:
                    curTurb = 1
                    maxTurb = max(maxTurb, curTurb)
                else:
                    sign = ">"
                    curTurb += 1
                    maxTurb = max(maxTurb, curTurb)
        
        return maxTurb