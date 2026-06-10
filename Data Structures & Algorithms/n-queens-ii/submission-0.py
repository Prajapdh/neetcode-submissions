class Solution:
    def totalNQueens(self, n: int) -> int:
        # Before placing a queen check if that positon is in threat:
        # horizontal: check if any queen has same row
        # vertical: check if any queen has same col
        # left-right-down diagonal: check if other queen has same x-y value
        # left-right-up diagonal: check if other queen has same x+y value
        queens = []
        res = [0]

        def checkConflict(row, col):
            for r, c in queens:
                if r == row or c == col or r - c == row - col or r + c == row + col:
                    return True
            return False

        def dfs(row):  # row = current row to place queen
            if row == n:
                res[0]+=1
                return
            
            # Try only columns for THIS specific row
            for col in range(n):
                if not checkConflict(row, col):
                    queens.append([row, col])
                    dfs(row + 1)  # Move to NEXT row
                    queens.pop()
        
        dfs(0)
        return res[0]
