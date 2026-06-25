class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # two pointers approach
        tPointer=0
        res=len(t)
        for r in range(len(s)):
            if tPointer<len(t) and s[r]==t[tPointer]:
                tPointer+=1
                res-=1
        return res
            