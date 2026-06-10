class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        rowLen=len(matrix[0])
        row=0
        l,r = 0, rowLen-1
        while(row<len(matrix) and l<=r):
            if(matrix[row][r]<target):
                row+=1
                continue
            
            m=(l+r)//2
            midEle = matrix[row][m]
            if(midEle>target):
                r=m-1
            elif(midEle<target):
                l=m+1
            else:
                return True
        
        return False