class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res=0
        # Add the sum of rectangle until (row2,col2)
        res+=self.sumMat[row2+1][col2+1]
        # Subract the rectange until (row1-1, col2)
        res-=self.sumMat[row1][col2+1]
        # Subract the left rectange, until (row2,col1-1)
        res-=self.sumMat[row2+1][col1]
        # We subracted the top left rectangle twice so add it again
        res+=self.sumMat[row1][col1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)