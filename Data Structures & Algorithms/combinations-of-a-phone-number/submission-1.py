class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad={'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}

        res=[]
        s=[]
        def dfs(i):
            if i==len(digits):
                res.append("".join(s))
                return
            for c in keypad[digits[i]]:
                s.append(c)
                dfs(i+1)
                s.pop()
        
        if digits: dfs(0)
        return res