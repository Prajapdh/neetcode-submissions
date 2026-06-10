class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxL=0
        countMap={}
        l=0
        maxF=0
        for r in range(len(s)):
            countMap[s[r]]=1 + countMap.get(s[r],0)
            maxF=max(countMap[s[r]], maxF)
            while((r-l+1)-maxF>k):
                countMap[s[l]]-=1
                l+=1
            maxL=max(maxL, r-l+1)
        
        return maxL
