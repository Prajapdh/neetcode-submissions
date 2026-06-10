class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join([char for char in s if char.isalnum()])
        s.lower()
        print(s)
        i,j=0, len(s)-1
        while(i<j):
            l,r = s[i], s[j]
            if ord(l) >= 65 and ord(l) <= 90:
                l = chr(ord(l) + 32)
            if ord(r) >= 65 and ord(r) <= 90:
                r = chr(ord(r) + 32)
            if(l!=r):
                print(f"l: {l}, r: {r}")
                return False
            i+=1
            j-=1
        return True