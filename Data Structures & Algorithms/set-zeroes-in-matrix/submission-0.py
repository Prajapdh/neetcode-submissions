class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
            ROWS, COLS = len(matrix), len(matrix[0])
            # Instead of having a seperate arrays to store zero-flags for rows and columns
            # We will use first row to store zeroflag for columns, and first col to store zeroflag for rows(skipping the first row as we are storing the value for 1st column)
            firstRow=1
            for i in range(ROWS):
                for j in range(COLS):
                    if i==0 and matrix[i][j]==0:
                        firstRow=0
                    elif matrix[i][j]==0:
                        matrix[i][0]=0  # flaging the row as zero in first column
                        matrix[0][j]=0  # flaging the col as zero in first row
            
            for i in range(1,ROWS):
                for j in range(1,COLS):
                    if matrix[i][0]==0 or matrix[0][j]==0:
                        matrix[i][j]=0
            if matrix[0][0]==0:
                for i in range(ROWS):
                    matrix[i][0]=0
                
            if firstRow==0:
                for j in range(COLS):
                    matrix[0][j]=0
            