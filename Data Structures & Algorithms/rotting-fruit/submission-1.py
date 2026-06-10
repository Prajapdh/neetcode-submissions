class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue=collections.deque()
        time=0
        fresh=0
     

        # add all rotten fruits in queue to perform multi source bfs
        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c]==2):
                    queue.append([r,c])
                if(grid[r][c]==1):
                    fresh+=1

        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and queue:
            length = len(queue)
            # traversing all cells in this layer
            for i in range(length):
                r, c = queue.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1
            time += 1
        
        return time if fresh==0 else -1