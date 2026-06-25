class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while stones and len(stones) > 1:
            s1 = stones.pop()
            s2 = stones.pop()
            if s1 - s2 == 0:
                continue
            stones.append(abs(s1 - s2))
        
        return stones[0] if stones else 0