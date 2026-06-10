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
            if r>=n:
                k=k%(n-l)
                r=l+(n-l-k)
                print(l,r,k,n)
        