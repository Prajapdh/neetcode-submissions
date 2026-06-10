class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars={}
        for i in s:
            if i not in chars.keys():
                chars[i] = 1
            else:
                chars[i] = chars[i]+1
        
        for j in t:
            if j not in chars.keys():
                return False
            elif(chars[j]==1):
                del chars[j]
            else:
                chars[j]=chars[j]-1;
        
        if(len(chars)==0):
            return True
        else:
            return False