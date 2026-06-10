class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i, n in enumerate(nums):
            if i>0 and nums[i-1]==n:
                continue
            l,r=i+1, len(nums)-1
            while(l<r):
                tsum = nums[i]+nums[l]+nums[r]
                if(tsum<0):
                    l+=1
                elif(tsum>0):
                    r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    #checking for duplicate numbers in between
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1

        return res