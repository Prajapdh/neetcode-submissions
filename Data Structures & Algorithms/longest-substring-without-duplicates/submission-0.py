class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        charSet=set(s[0])
        l,r=0,1
        res=1
        while l<r and r<len(s):
            while s[r] in charSet:
                # print(res, s[l:r])
                charSet.remove(s[l])
                l+=1
            res=max(res, r-l+1)
            charSet.add(s[r])
            r+=1
        
        return res
