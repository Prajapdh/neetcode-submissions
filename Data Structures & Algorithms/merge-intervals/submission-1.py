class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort()
        newInterval=intervals[0]
        for i in range(1, len(intervals)):
            if(newInterval[1]<intervals[i][0]):
                res.append(newInterval)
                newInterval=intervals[i]
            elif(newInterval[1]>=intervals[i][0]):
                newInterval=[min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res