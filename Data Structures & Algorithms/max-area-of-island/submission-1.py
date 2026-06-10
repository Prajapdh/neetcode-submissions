class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Use BFS
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        directions=[[0,1], [0,-1], [1,0], [-1,0]]
        res=0

        def bfs(r,c):
            # print(r,c)
            queue=collections.deque()
            queue.append([r,c])
            grid[r][c]=0
            area=1
            while queue:
                r,c=queue.popleft()
                print(grid, r, c)
                for rs,cs in directions:
                    nr, nc= r+rs, c+cs
                    if(nr<0 or nc<0 or nr>=ROWS or nc>=COLS or (grid[nr][nc]==0)):
                        continue
                    grid[nr][nc]=0
                    queue.append([nr,nc])
                    area+=1
            print(area)
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c]==1):
                    # print("bfs")
                    res=max(res, bfs(r,c))
        
        return res
