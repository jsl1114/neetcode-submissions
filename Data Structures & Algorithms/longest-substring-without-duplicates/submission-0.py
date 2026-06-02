class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        for i,c in enumerate(s):
            index = i + 1
            cur_longest = 1
            exist = [c]
            while index < len(s) and s[index] not in exist:
                exist.append(s[index])
                cur_longest += 1
                index += 1
            longest = cur_longest if cur_longest > longest else longest
        
        return longest
            


