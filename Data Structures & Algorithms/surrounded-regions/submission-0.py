class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Find the 'O' that are at the borders
        # visit all 'O' related to that border 'O'
        # Convert all 'O' to 'X' that are not visited before
        ROWS, COLS = len(board), len(board[0])
        visited=set()
        def dfs(row, col):
            if(row<0 or col<0 or row>=ROWS or col>=COLS or ((row, col) in visited) or board[row][col]!='O'):
                return
            visited.add((row, col))
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        # Traversing to all border cells
        for c in range(COLS):
            if(board[0][c]=='O'): dfs(0,c)
            if(board[ROWS-1][c]=='O'): dfs(ROWS-1, c)
        
        for r in range(1, ROWS-1):
            if(board[r][0]=='O'): dfs(r, 0)
            if(board[r][COLS-1]): dfs(r, COLS-1)

        # Convert all unvisited 'O' to 'X'
        for r in range(ROWS):
            for c in range(COLS):
                if(board[r][c]=='O' and ((r,c) not in visited)): board[r][c]='X'
