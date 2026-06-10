class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxL=0
        countMap={}
        l=0
        for r in range(len(s)):
            countMap[s[r]]=1 + countMap.get(s[r],0)
            while((r-l+1)-max(countMap.values())>k):
                countMap[s[l]]-=1
                l+=1
            maxL=max(maxL, r-l+1)
        
        return maxL
