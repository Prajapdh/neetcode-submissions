class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # store all '0' at edges, run BFS on them, store their adjacent '0's as unclaimed
        # traverse through whole matrix, mark 'X' if cell is not present in unclaimed
        ROWS, COLS = len(board), len(board[0])
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        queue=collections.deque()
        visited=set()

        for i in range(ROWS):
            if(board[i][0]=='O'):
                queue.append((i,0))
            if(board[i][COLS-1]=='O'):
                queue.append((i, COLS-1))
        
        for j in range(1, COLS-1):
            if(board[0][j]=='O'):
                queue.append((0,j))
            if(board[ROWS-1][j]=='O'):
                queue.append((ROWS-1, j))
        
        while queue:
            r,c = queue.popleft()
            visited.add((r,c))
            for dx, dy in directions:
                x, y = r+dx, c+dy
                if(0<=x<ROWS and 0<=y<COLS and ((x,y) not in visited) and board[x][y]=='O'):
                    visited.add((x,y))
                    queue.append((x,y))
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited:
                    board[i][j]='X'