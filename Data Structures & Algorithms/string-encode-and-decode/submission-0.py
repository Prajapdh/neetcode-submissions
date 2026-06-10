class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res, cs = [], "", ""
        for s in strs:
            sizes.append(len(s))
            cs+=s
        for size in sizes:
            res+=str(size)+','
        res= res + '#'
        res+=cs
        # print(res)
        return res


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while i<len(s) and s[i]!='#':
            buff=""
            while i<len(s) and s[i]!=',' and s[i]!='#':
                buff+=s[i]
                i+=1
            sizes.append(int(buff))
            i+=1
        i+=1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res

