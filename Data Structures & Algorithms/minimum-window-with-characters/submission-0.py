class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # handeling edge case
        if(t==""): return ""

        have, need = 0,0
        countT, countS={}, {}
        # update the countT map
        for c in t:
            countT[c]= 1+countT.get(c, 0)
        
        # update the need score
        need = len(countT)

        res, resLen=[-1,-1], float("inf")
        l=0
        for r in range(len(s)):
            c=s[r]
            countS[c]=1+countS.get(c, 0)
            # update the have counter only if required char is found
            if c in countT and countS[c]==countT[c]:
                have+=1
            
            while have==need:
                # if current length is less than resLen, we update our values
                lenn=r-l+1
                if(lenn<resLen):
                    res=[l,r]
                    resLen=lenn
                # lets remove the leftmost char to reduce our window size
                countS[s[l]]-=1
                if s[l] in countT and countS[s[l]]<countT[s[l]]:
                    have-=1

                l+=1
        
        return s[res[0]: res[1]+1] if resLen!=float("inf") else ""