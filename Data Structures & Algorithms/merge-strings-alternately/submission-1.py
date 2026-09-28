class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        i=0
        res=""
        while(i<min(l1,l2)):
            res+=word1[i]+word2[i]
            i+=1
        while(i<l1):
            res+=word1[i]
            i+=1
        while(i<l2):
            res+=word2[i]
            i+=1
        
        return res