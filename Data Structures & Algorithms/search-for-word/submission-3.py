class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions=[[1,0], [-1,0],[0,1], [0,-1]]
        visited=set()
        def dfs(r,c,i):
            if i>len(word) or r<0 or r>=ROWS or c<0 or c>=COLS or ((r,c) in visited) or board[r][c]!=word[i]:
                return False
            if i==len(word)-1:
                print(r,c,i)
                return True
            visited.add((r,c))
            res=False
            for x,y in directions:
                res = res or dfs(r+x, c+y, i+1)
            visited.remove((r,c))
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True
        
        return False
            