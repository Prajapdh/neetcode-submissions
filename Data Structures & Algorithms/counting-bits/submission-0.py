class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for num in range(n+1):
            cnt=0
            while num!=0:
                if num&1==1:
                    cnt+=1
                num=num>>1
            res.append(cnt)
        return res