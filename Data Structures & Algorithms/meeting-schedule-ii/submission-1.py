"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms=[]
        if not intervals:
            return len(rooms)
        intervals.sort(key=lambda interval: interval.end)
        rooms.append(intervals[0].end)
        for i in range(1, len(intervals)):
            flag=False
            print(rooms)
            for room, endTime in enumerate(rooms):
                if endTime<=intervals[i].start:
                    rooms[room]=intervals[i].end
                    flag=True
                    break
            if not flag: rooms.append(intervals[i].end)
        
        return len(rooms)
