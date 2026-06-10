class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Before placing a queen check if that positon is in threat:
        # horizontal: check if any queen has same row
        # vertical: check if any queen has same col
        # left-right-down diagonal: check if other queen has same x-y value
        # left-right-up diagonal: check if other queen has same x+y value
        board = [['.' for _ in range(n)] for _ in range(n)]
        queens = []
        res = []

        def checkConflict(row, col):
            for r, c in queens:
                if r == row or c == col or r - c == row - col or r + c == row + col:
                    return True
            return False

        def dfs(row):  # row = current row to place queen
            if row == n:
                res.append(["".join(rw) for rw in board])
                return
            
            # Try only columns for THIS specific row
            for col in range(n):
                if not checkConflict(row, col):
                    queens.append([row, col])
                    board[row][col] = 'Q'
                    dfs(row + 1)  # Move to NEXT row
                    board[row][col] = '.'
                    queens.pop()
        
        dfs(0)
        return res
