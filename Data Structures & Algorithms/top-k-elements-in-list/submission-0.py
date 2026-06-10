class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums.sort()
        # i,j=0, 0
        # k,maxc=nums[i],1
        # for n in nums:
        #     if nums[i]==nums[j]==n:
        #         j+=1
        #     elif(nums[j]!=n):
        #         if maxc>(j-i):
        #             maxc=j-i
        #             k=nums[i]
        #             i=j
        # return k
        if k>len(nums):
            return []
        count = {}
        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n]=0
        count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        print(f"Count: {count}")
        topK=[]
        for i in count.keys():
            if  k==0:
                break
            topK.append(i)
            k-=1
        return topK