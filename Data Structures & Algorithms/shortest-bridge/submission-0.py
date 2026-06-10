class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # size of grid? min distance is 1?
        # find two points closest to each other in islands to connect them
        # Initial approach: start from 1st island, do a BFS and return the shortest path to another island
        # how to differenciate between two islands? traverse the matrix until you find first 1, add it to visited, run BFS- all cells of first island acquired
        ROWS, COLS= len(grid), len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def findFirstIsland(grid):
            queue=collections.deque()
            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j]==1:
                        queue.append((i,j))
                        break
                if queue:
                    break
            res=[]
            visited=set()
            while queue:
                x,y=queue.popleft()
                visited.add((x,y))
                res.append((x,y))
                for dx,dy in directions:
                    nx,ny=x+dx, y+dy
                    if 0<=nx<ROWS and 0<=ny<COLS and grid[nx][ny]==1 and ((nx,ny) not in visited):
                        queue.append((nx,ny))
                        visited.add((nx,ny))
            return res
        
        # Run BFS from first island
        firstIsland=findFirstIsland(grid)
        # print(firstIsland)
        visited=set(firstIsland)
        queue=collections.deque(firstIsland)
        path=-1
        while queue:
            size=len(queue)
            path+=1
            for _ in range(size):
                x,y=queue.popleft()
                visited.add((x,y))
                for dx,dy in directions:
                    nx,ny=x+dx, y+dy
                    if 0<=nx<ROWS and 0<=ny<COLS and ((nx,ny) not in visited):
                        if grid[nx][ny]==1:
                            return path
                        else:
                            queue.append((nx,ny))
                            visited.add((nx,ny))
        
        return -1