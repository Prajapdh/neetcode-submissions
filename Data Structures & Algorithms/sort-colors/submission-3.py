class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # To divide these buckets in one pass we have to take inspiration from quick sort's partition
        # We will have 3 pointers: everything to the left of L is 0, everything to the right of R is 2 and i will be our traversing pointer
        l,r,i=0, len(nums)-1,0

        # We only traaverse until r poniter cause everything to the right is alredy 2
        while r>=0 and i<=r:
            # check if nums[i]==0, if yes then swap it with l index and increment l and r
            if nums[i]==0:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
            # check if nums[i]==2, if yes then we swap it with r index
            elif nums[i]==2:
                nums[i],nums[r]=nums[r],nums[i]
                # We will only decrement r and not increase i cause we don't want to skip whatever we jsut replaced
                # We don't need to to take care of this for the lth case cause we will always 0 or 1, any 2s will be already replaced until l gets there
                r-=1
                i-=1
            i+=1
            # print(l,i,r)
            # print(nums)