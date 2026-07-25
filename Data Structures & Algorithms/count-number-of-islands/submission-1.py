class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def bfs(i,j):
            queue = collections.deque([(i,j)])
            grid[i][j]='0'
            while queue:
                x,y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<ROWS and 0<=ny<COLS and grid[nx][ny]=='1':
                        grid[nx][ny]='0'
                        queue.append((nx,ny))
        res=0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=='1':
                    bfs(i,j)
                    res+=1
        
        return res