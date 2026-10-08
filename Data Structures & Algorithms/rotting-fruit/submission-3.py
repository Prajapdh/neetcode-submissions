class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh=0
        rotten=0
        queue=collections.deque()   #rotten fruits

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    rotten+=1
                    queue.append((i,j))
        
        time=0
        directions=[[-1,0], [1,0], [0,-1], [0,1]]
        while fresh>0 and queue:
            size=len(queue)
            
            for _ in range(size):
                x,y = queue.popleft()
                for dx, dy in directions:
                    p,q = x+dx, y+dy
                    if 0<=p<ROWS and 0<=q<COLS and grid[p][q]==1:
                        fresh-=1
                        rotten+=1
                        grid[p][q]=2
                        queue.append((p,q))
            time+=1
            
        
        return time if fresh==0 else -1