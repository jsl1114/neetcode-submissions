"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 1:
            return True

        startAsc = [interval for interval in sorted(intervals, key=lambda i: i.start)]
        for i in range(1, len(startAsc)):
            if startAsc[i-1].end > startAsc[i].start:
                return False
        
        return True