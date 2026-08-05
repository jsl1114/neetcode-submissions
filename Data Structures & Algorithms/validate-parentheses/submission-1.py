class Solution:
    def isValid(self, s: str) -> bool:
        valids = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        stack = []

        for c in s:
            if c in valids.values():
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    match = stack.pop(-1)
                    if valids[c] != match:
                        return False

        return len(stack) == 0