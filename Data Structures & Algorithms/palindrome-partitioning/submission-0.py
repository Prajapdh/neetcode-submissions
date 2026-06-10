class Solution:
    def isPalindrome(self, s:  str, l: str, r: str)->bool:
        while(l<r):
            if(s[l]!=s[r]):
                return False
            l+=1
            r-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res=[]
        curr=[]
        def dfs(i):
            if i>=len(s):
                res.append(curr.copy())
                print("accepted ",curr)
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    curr.append(s[i:j+1])
                    print(curr)
                    dfs(j+1)
                    curr.pop()
        
        dfs(0)                  


        return res