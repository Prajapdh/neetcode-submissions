class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sortedQueries=sorted((queries[i],i) for i in range(len(queries)))
        # print(sortedQueries)
        intervals.sort()
        res=[-1]*len(queries)
        minHeap=[]
        intervalPointer, queryPointer = 0,0
        print(intervals)
        
        for q, queryIndex in sortedQueries:
            print(q, queryIndex)
            # adding the interval to heap if it starts now or in past
            while intervalPointer < len(intervals) and intervals[intervalPointer][0] <= q:
                l, r = intervals[intervalPointer]
                # we will add a pair to the heap: (distance, endPoint)
                heapq.heappush(minHeap, (r - l + 1, r))
                intervalPointer += 1

            # if the endPoint of the shortest interval is in the past, we will pop it
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[queryIndex] = minHeap[0][0] if minHeap else -1

        return res