class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            if nums[i]>0:
                break
            j=i+1
            k=len(nums)-1
            while j<k:
                currSum=nums[i]+nums[j]+nums[k]
                if currSum==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while 0<k<len(nums)-1 and nums[k+1]==nums[k]:
                        k-=1
                    while len(nums)>j>i+1 and nums[j-1]==nums[j]:
                        j+=1
                elif currSum>0:
                    k-=1
                else:
                    j+=1
                    
        return res