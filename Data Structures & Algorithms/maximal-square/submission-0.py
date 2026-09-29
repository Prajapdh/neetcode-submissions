class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        squareSum=[[0]*COLS for _ in range(ROWS)]
        maxSize=0
        for i in range(ROWS-1,-1,-1):
            for j in range(COLS-1,-1,-1):
                    if(matrix[i][j]=='0'):
                        squareSum[i][j]=0
                    else:
                        down=squareSum[i+1][j] if i+1<ROWS else 0
                        right=squareSum[i][j+1] if j+1<COLS else 0
                        diag=squareSum[i+1][j+1] if(j+1<COLS and i+1<ROWS) else 0
                        squareSum[i][j]=1+min(down, right, diag)
                        maxSize = max(maxSize,squareSum[i][j])
        
        return maxSize**2