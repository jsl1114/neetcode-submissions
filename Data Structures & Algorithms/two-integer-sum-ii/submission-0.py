class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = [0,0]
        cur_sum = numbers[res[0]] + numbers[res[1]]
        
        while cur_sum != target:
            if cur_sum < target:
                res[0] += 1
                res[1] += 2
            else:
                res[1] -= 1
            cur_sum = numbers[res[0]] + numbers[res[1]]
        
        res[0] += 1
        res[1] += 1
        res.sort()

        return res
                
