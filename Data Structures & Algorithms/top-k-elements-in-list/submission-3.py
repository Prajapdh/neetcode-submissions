class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Lets store the count of each element
        counter={}
        for n in nums:
            if n not in counter:
                counter[n]=0
            counter[n]+=1
        
        # Maximum number of times an element will occur is the size of nums
        freq=[[] for _ in range(len(nums)+1)] #empty buckets which will store the number with index as number of times an element appears
        for ele, cnt in counter.items():
            freq[cnt].append(ele)

        
        res=[]
        i=len(nums)
        while i>=0 and k>0:
            if freq[i]:
                for j in range(len(freq[i])):
                    if k>0:
                        res.append(freq[i][j]);
                        k-=1
                    else:
                        break
            i-=1
        
        return res