class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Lets store the counter of all tasks
        counter={}
        for t in tasks:
            counter[t]=counter.get(t,0)-1
        
        # We will store it in the maxHeap as we always want to execute the task with largest number
        maxHeap=[]
        for key in counter.keys():
            heapq.heappush(maxHeap, (counter[key], key))
        
        waitingQueue=collections.deque()    # endTime, TaskName, numLeft
        time=0

        while maxHeap or waitingQueue:
            time+=1
            if maxHeap:
                numLeft, task = heapq.heappop(maxHeap)
                if numLeft+1:
                    waitingQueue.append((time+n, task, numLeft+1))

            if waitingQueue and waitingQueue[0][0]==time:
                e, task, numLeft = waitingQueue.popleft()
                heapq.heappush(maxHeap, (numLeft, task))
            # elif(waitingQueue and (not maxHeap)):
            #     time=max(time, waitingQueue[0][0])


        return time
