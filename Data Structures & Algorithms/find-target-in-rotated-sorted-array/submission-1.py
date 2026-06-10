class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0, len(nums)-1
        while(l<r):
            m=(l+r)//2
            if(nums[m]>nums[r]):
                # Pivot point is to the right
                l=m+1
            else:
                r=m

        pivotIndex=l
        # print(f"Pivot: {pivotIndex}")
        if(pivotIndex==0):
            l=0
            r=len(nums)-1     
        elif(target>=nums[0] and target<=nums[pivotIndex-1]):
            l=0
            r=pivotIndex-1
        else:
            l=pivotIndex
            r=len(nums)-1
        
        while(l<=r):
            m=(l+r)//2
            print(l,m,r)
            if(nums[m]<target):
                l=m+1
            elif(nums[m]>target):
                r=m-1
            else:
                return m
        return -1