class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have=0
        need=len(t)
        sCounter=defaultdict(int)
        tCounter=defaultdict(int)
        for c in t:
            tCounter[c]+=1
        
        l=r=0
        res=s+t
        while r<len(s):
            if(tCounter[s[r]]>sCounter[s[r]]):
                have+=1
            sCounter[s[r]]+=1
            while have==need and l<=r:
                if(len(res)>=r-l+1):
                    res=s[l:r+1]
                sCounter[s[l]]-=1
                if(tCounter[s[l]]>sCounter[s[l]]):
                    have-=1
                l+=1
            r+=1

        return res if len(res)<len(s)+len(t) else ""