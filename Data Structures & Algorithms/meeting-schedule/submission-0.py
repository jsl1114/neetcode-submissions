"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_ints = [interval for interval in sorted(intervals, key=lambda i: i.start)]
        end = 0
        for i in sorted_ints:
            if end > i.start:
                return False
            else:
                end = i.end
        
        return True