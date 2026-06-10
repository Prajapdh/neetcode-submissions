class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l,r = 0, 0
        res=0
        while l<=r and r<len(s):
            while window and s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            res=max(res, r-l+1)
            r+=1
        return res