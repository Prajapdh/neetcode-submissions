class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid: return

        ROWS, COLS= len(grid), len(grid[0])
        directions=[[0,1], [0,-1], [1,0], [-1,0]]
        def bfs(row,col):
            queue=deque()
            queue.append([row,col,0])
            visited=set()
            visited.add((row,col))
            while(queue):
                row, col, distance= queue.popleft()
                for rs,cs in directions:
                    nr,nc=rs+row, cs+col
                    if(nr<0 or nc<0 or nr>=ROWS or nc>=COLS or ((nr,nc) in visited) or grid[nr][nc]==-1 or grid[nr][nc]==0):
                        continue
                    visited.add((nr,nc))
                    grid[nr][nc]=min(grid[nr][nc], distance+1)
                    queue.append([nr,nc,distance+1])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    bfs(r,c)
                