class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        ret = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff

            if total < 0:
                ret = i + 1
                total = 0
        
        return ret