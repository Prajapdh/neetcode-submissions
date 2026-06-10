class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Lets have two pointers l and r
        # if we find that values at both pointers aren't equal then we will compare string strings by skipping element at lth or rth index
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skipL=s[l+1:r+1]    #skip l, include rth index
                skipR=s[l:r]    #r is excluded
                return skipL==skipL[::-1] or skipR==skipR[::-1]
            l+=1
            r-=1
        return True