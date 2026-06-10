class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyMap={2:['a', 'b', 'c'],
        3:['d','e','f'],
        4:['g','h','i'],
        5:['j','k','l'],
        6:['m','n','o'],
        7:['p','q','r','s'],
        8:['t','u','v'],
        9:['w','x','y','z']}

        res=[]

        def dfs(d, curr):
            if not d:
                res.append(curr)
                return
            digit=int(d[0])
            for c in keyMap[digit]:
                curr+=c
                dfs(d[1:], curr)
                curr=curr[:len(curr)-1]
        
        if digits: dfs(digits, "")
        return res