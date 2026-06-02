"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        dic = defaultdict(int)
        cur = ret = 0

        for i in intervals:
            dic[i.start] += 1
            dic[i.end] -= 1
        
        for k in sorted(dic):
            cur += dic[k]
            ret = max(ret, cur)
        
        return ret