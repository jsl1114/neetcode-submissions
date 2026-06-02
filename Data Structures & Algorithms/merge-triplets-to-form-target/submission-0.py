class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ta, tb, tc = target
        possible = []
        for a, b, c in triplets:
            if any([a > ta, b > tb, c > tc]):
                continue
            possible.append([a, b, c])
        
        met = [False, False, False]

        for a, b, c in possible:
            if a == ta:
                met[0] = True
            if b == tb:
                met[1] = True
            if c == tc:
                met[2] = True
            if all(met):
                return True
        
        return False