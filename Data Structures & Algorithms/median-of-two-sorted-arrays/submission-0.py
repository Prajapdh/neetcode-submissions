class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total=len(nums1)+len(nums2)
        half= total//2
        A,B = nums1, nums2

        if(len(B)<len(A)):
            A,B = B, A  #swapping arrays cause we only want to perform search on min len array
        
        l,r=0, len(A)-1
        while True:
            i=(l+r)//2
            j=half-i-2  #becasue arrays start with index 0

            aLeft= A[i] if i>=0 else float("-inf")
            aRight = A[i+1] if (i+1)<len(A) else float("inf")
            bLeft= B[j] if j>=0 else float("-inf")
            bRight = B[j+1] if (j+1)<len(B) else float("inf")

            #correct partition
            if aLeft<=bRight and bLeft<=aRight:
                #odd len
                if(total%2):
                    return min(aRight, bRight)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight))/2
            #incorrect partitions
            elif aLeft>bRight:
                r=i-1
            else:
                l=i+1


