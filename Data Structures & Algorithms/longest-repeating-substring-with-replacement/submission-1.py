class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxL=0
        countMap={}
        l=0
        for r in range(len(s)):
            countMap[s[r]]=1 + countMap.get(s[r],0)
            if((r-l+1)-max(countMap.values())<=k):
                maxL=max(maxL, r-l+1)
            else:
                print(l,r,s[r])
                countMap[s[l]]-=1
                l+=1
        
        return maxL
