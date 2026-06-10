class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # can only move down or right
        # reach bottom-right from top-left, minimize the path sum
        # base case: (r==ROWS-1 and c==COLS) or (r==ROWS and c==COLS-1)
        ROWS, COLS = len(grid), len(grid[0])
        memo=[[float('inf') for _ in range(COLS+1)] for _ in range(ROWS+1)]
        memo[ROWS-1][COLS]=0
        memo[ROWS][COLS-1]=0
        def dfs(r,c):
            if (r==ROWS-1 and c==COLS) or (r==ROWS and c==COLS-1):
                return 0
            elif (r>=ROWS or c>=COLS):
                return float('inf')
            elif memo[r][c]!=float('inf'):
                return memo[r][c]        
            currSum=grid[r][c]
            currSum+=min(dfs(r,c+1), dfs(r+1,c))
            memo[r][c]=currSum
            return currSum
        
        return dfs(0,0)