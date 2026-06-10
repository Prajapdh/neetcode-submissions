class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        l,r=0,(n-k)
        while r<n and l<n:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r+=1
            # until this point, first k elements are in correct place
            # But if k=2(l=3) array looks like: [7,8,3,4,5,6,1,2], We want to rotate the subarray from left pointer
            # Since we have new length, we update the value of k and update the r pointer
            # There will be case when length of subarray is 1, the new r will be greater than n so we stop
            if r>=n:
                k=k%(n-l)
                r=l+(n-l-k)
                print(l,r,k,n-l)
        