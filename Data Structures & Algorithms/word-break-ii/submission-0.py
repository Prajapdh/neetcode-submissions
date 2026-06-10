class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet=set(wordDict)
        n=len(s)
        res=[]
        sentence=[]
        def dfs(i, word):
            if i==n:
                if not word:
                    res.append(" ".join(sentence))
                return
            for j in range(i,n):
                word+=s[j]
                if word in wordSet:
                    sentence.append(word)
                    dfs(j+1, "")
                    sentence.pop()
        dfs(0,"")
        return res