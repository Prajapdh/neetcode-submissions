class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res=[]
        i=0
        while i<len(nums)-2:
            if nums[i] > 0:  # Early termination
                break
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate i
                i += 1
                continue
            j,k=i+1,len(nums)-1
            while j<k:
                addition=nums[i]+nums[j]+nums[k]
                if addition==0:
                    res.append([nums[i],nums[j],nums[k]])
                    # Skip duplicates for j and k
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif addition>0:
                    k-=1
                else:
                    j+=1
            i+=1
        return res