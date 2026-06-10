class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        threshold=n//3
        counter={}
        res=set()
        for i in range(n):
            if nums[i] not in counter:
                counter[nums[i]]=0
            counter[nums[i]]+=1
            if counter[nums[i]]>threshold:
                res.add(nums[i])
        
        return list(res)