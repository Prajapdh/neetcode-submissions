class NumMatrix:
    # Precompute sum of rectange formed by (0,0) and (r,c) at (r,c) in new matrix
    # Then find the sum of any given rectangle by subracting other rectangles(unwanted area)
    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.ROWS, self.COLS = len(matrix), len(matrix[0])
        self.rectangleSum=[[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.computeRectangleSum()
        print(self.rectangleSum)
    
    def computeRectangleSum(self):
        # sum of given rectangle: matrix[r,c] + top cell + prefixSum until this cell in given row
        for i in range(self.ROWS):
            prefixSum=0
            for j in range(self.COLS):
                # Add top cell
                self.rectangleSum[i][j]=self.rectangleSum[i-1][j] if i>0 else 0
                # Add prefixSUm
                self.rectangleSum[i][j]+=prefixSum
                self.rectangleSum[i][j]+=self.matrix[i][j]
                prefixSum+=self.matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # res: sum for rec(row2,col2) - rec(row1-1,col2) - rec(row2,col1-1) + rec(row1-1, col1-1)
        res=self.rectangleSum[row2][col2]
        res-=self.rectangleSum[row1-1][col2] if row1>0 else 0
        res-=self.rectangleSum[row2][col1-1] if col1>0 else 0
        res+=self.rectangleSum[row1-1][col1-1] if row1>0 and col1>0 else 0
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)