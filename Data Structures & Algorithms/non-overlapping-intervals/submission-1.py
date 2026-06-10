class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        res=0
        prevEnd=intervals[0][1]
        for start, end in intervals[1:]:
            # not overlapping
            if(prevEnd<=start):
                prevEnd=end
            # overlapping intervals found
            else:
                res+=1
                # removing the interval with greater end value
                prevEnd= min(end, prevEnd)
        
        return res