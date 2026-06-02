class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedPos = [0] * len(position)
        ret = []

        for i in range(len(speedPos)):
            speedPos[i] = (speed[i], position[i])
        
        speedPos.sort(key=lambda x: -x[1])

        for curSpeed, curPos in speedPos:
            time = (target - curPos) / curSpeed
            if len(ret) == 0 or time > ret[-1]:
                ret.append(time)
        
        return len(ret)

