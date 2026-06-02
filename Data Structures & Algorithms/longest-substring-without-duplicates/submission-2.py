class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ret = 0
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            ret = max(ret, r - l + 1)

        return ret