class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
                continue
            
            # If end time of last interval if more than start time of curr interval, merge them
            if res[-1][1]>=intervals[i][0]:
                res[-1][1]=max(intervals[i][1],res[-1][1])
            else:
                res.append(intervals[i])
        
        return res