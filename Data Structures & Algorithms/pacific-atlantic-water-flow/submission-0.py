class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions=[[0,1], [0,-1], [1,0], [-1,0]]
        pVisited, aVisited = set(), set()
        pQueue, aQueue = deque(), deque()
        # add the top and left edge to pVisited
        for c in range(COLS):
            pVisited.add((0,c))
            pQueue.append([0,c])
        for r in range(1, ROWS):
            pVisited.add((r,0))
            pQueue.append([r,0])
        # add the bottom and right edge to aVisited
        for c in range(COLS):
            aVisited.add((ROWS-1,c))
            aQueue.append([ROWS-1,c])
        for r in range(ROWS-1):
            aVisited.add((r,COLS-1))
            aQueue.append([r,COLS-1])
        # print(pVisited)
        # print(aVisited)

        # running BFS, we will only visit the cell if its height is greater than the current height
        # All visited cell are capable of flowing water to their respective ocean
        while pQueue:
            row, col = pQueue.popleft()
            height=heights[row][col]
            for rOff, cOff in directions:
                nr, nc = row+rOff, col+cOff
                if(nr<0 or nc<0 or nr>=ROWS or nc>=COLS or heights[nr][nc]<height or ((nr,nc) in pVisited)):
                    continue
                pVisited.add((nr,nc))
                pQueue.append([nr, nc])
        

        while aQueue:
            row, col = aQueue.popleft()
            height=heights[row][col]
            for rOff, cOff in directions:
                nr, nc = row+rOff, col+cOff
                if(nr<0 or nc<0 or nr>=ROWS or nc>=COLS or heights[nr][nc]<height or ((nr,nc) in aVisited)):
                    continue
                aVisited.add((nr,nc))
                aQueue.append([nr, nc])
        
        return list(pVisited.intersection(aVisited))
