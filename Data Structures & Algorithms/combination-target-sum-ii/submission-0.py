class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() # so that duplicates are together

        def backtrack(start, targetLeft, path):
            if targetLeft == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]: # dup, skip
                    continue
                
                if candidates[i] > targetLeft:
                    break
                
                path.append(candidates[i])
                backtrack(i+1, targetLeft - candidates[i], path)
                path.pop()
        
        backtrack(0, target, [])

        return res
