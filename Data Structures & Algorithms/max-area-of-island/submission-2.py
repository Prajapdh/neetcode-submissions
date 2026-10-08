class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res=0
        if not grid:
            return [0]
        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        def bfs(i,j):
            queue=collections.deque([(i,j)])
            area=0
            while queue:
                x,y = queue.popleft()
                area+=1
                grid[x][y]=0
                for dx, dy in directions:
                    p,q = x+dx, y+dy
                    if 0<=p<ROWS and 0<=q<COLS and grid[p][q]:
                        grid[p][q]=0
                        queue.append((p,q))
            
            return area
        
        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j]):
                    res=max(res, bfs(i,j))
        
        return res