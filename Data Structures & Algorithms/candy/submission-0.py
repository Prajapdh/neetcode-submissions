class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        res=[1]*n
        for i in range(n):
            candy=1
            j=1
            while i-j>=0 and ratings[i-j+1]<ratings[i-j] and res[i-j+1]>=res[i-j]:
                print(i-j)
                res[i-j]+=1
                j+=1
            if i-1>=0 and ratings[i-1]<ratings[i]:
                candy+=res[i-1]-res[i]+1
            res[i]=candy
        print(res)
        return sum(res)
