class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Brute force: O(n)
        # Binary Search: if mid is greater than left, peak is at right; if mid is less than right, peak is left to the mid; else mid is peak
        n=len(nums)
        l=0
        r=n-1
        while(l<r):
            mid=(r-l)//2+l
            leftEle = nums[mid-1] if(mid-1>=0) else float('-inf')
            rightEle = nums[mid+1] if(mid+1<n) else float('-inf')
            if(leftEle<nums[mid] and nums[mid]>rightEle):
                return mid
            elif(nums[mid]<rightEle):
                l=mid+1
            else:
                r=mid-1
        
        return l