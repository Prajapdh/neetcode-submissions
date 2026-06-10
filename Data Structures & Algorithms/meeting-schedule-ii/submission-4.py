"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals=sorted(intervals, key= lambda x: x.start)
        minHeap=[intervals[0].end]
        i,res=1,1
        while minHeap and i<len(intervals):
            end=minHeap[0]
            if intervals[i].start>=end:
                heapq.heappop(minHeap)

            heapq.heappush(minHeap, intervals[i].end)
            res=max(res, len(minHeap))
            print(intervals[i].start, intervals[i].end, minHeap, res)
            i+=1
        return res