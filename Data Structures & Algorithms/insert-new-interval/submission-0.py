class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not newInterval:
            return intervals
        n= len(intervals)
        res=[]
        for i in range(n):
            # print(newInterval)
            # if new interval comes before ith interval
            if(newInterval[1]<intervals[i][0]):
                res.append(newInterval)
                # add rest of the intervals to result
                return res+intervals[i:]
            # if the new interval comes after the ith interval
            elif (newInterval[0]>intervals[i][1]):
                res.append(intervals[i])
            # if its overlapping
            else:
                newInterval=[min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        # if the newInterval is the last interval
        res.append(newInterval)
        return res