class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeedDesc = sorted(list(zip(position, speed)), key=lambda x: x[0], reverse=True)
        stack = []

        for i in range(len(position)):
            timeTillArrival = (target - posSpeedDesc[i][0]) / posSpeedDesc[i][1]
            if not stack or timeTillArrival > stack[-1]:
                stack.append(timeTillArrival)
        
        return len(stack)
