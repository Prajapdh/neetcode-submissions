class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Since we have to do this inplace, lets start adding elements from the end
        p1,p2,i=m-1,n-1,m+n-1

        while i>=0 and p1>=0 and p2>=0:
            if nums1[p1]>nums2[p2]:
                nums1[i]=nums1[p1]
                p1-=1
            else:
                nums1[i]=nums2[p2]
                p2-=1
            i-=1
        
        # Don't care about remaining elements(to the left of p1) as they are already in place
        # We only add remaining elements from nums2
        while p2>=0 and i>=0:
            nums1[i]=nums2[p2]
            p2-=1
            i-=1
