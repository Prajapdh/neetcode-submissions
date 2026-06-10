class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1Counter = [0]*26
        for c in s1:
            s1Counter[ord(c)-ord('a')]+=1
        
        l=0
        s2Counter = [0]*26
        for r in range(len(s2)):
            s2Counter[ord(s2[r])-ord('a')]+=1
            while s1Counter[ord(s2[r])-ord('a')]<s2Counter[ord(s2[r])-ord('a')]:
                s2Counter[ord(s2[l])-ord('a')]-=1
                l+=1
            flag=True
            for i in range(len(s1Counter)):
                if s1Counter[i]!=s2Counter[i]:
                    flag=False
                    break
            if flag:
                return True
        return False