class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        print(nums)
        res=[]
        for i in range(n-3):
            if nums[i]>target:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if nums[i]+nums[j]>target:
                    break
                #only compare with last jth index not ith
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k,l=j+1, n-1
                while k<l:
                    diff=target-(nums[i]+nums[j]+nums[k]+nums[l])
                    print(i,j,k,l,diff)
                    if diff==0:
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while k<l+1<n and nums[l]==nums[l+1]:
                            l-=1
                    elif diff>0:
                        k+=1
                    else:
                        l-=1
        return res