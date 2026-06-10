class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=len(t)
        reqMap=defaultdict(int)
        window=defaultdict(int)
        for c in t:
            reqMap[c]=1+reqMap.get(c,0)
        curr=0
        l=0
        minLen=float('inf')
        res=""
        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)
            if window[s[r]]<=reqMap[s[r]]:
                curr+=1
            while curr==need:
                print("curr: ", curr, " string: ", s[l:r+1], r-l+1, len(res))
                if r-l+1<=minLen:
                    res=s[l:r+1]
                    minLen=len(res)
                window[s[l]]-=1
                if window[s[l]]<reqMap[s[l]]:
                    curr-=1
                l+=1
        return res