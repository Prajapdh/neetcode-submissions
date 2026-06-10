class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Using sliding window
        # we store the sum of differances and update the result array if currDiff is smaller than min diff
        minDiff=float('inf')
        l=0
        res=[]
        currDiff=0
        for r in range(len(arr)):
            currDiff+=abs(x-arr[r])
            if r-l+1==k:
                if currDiff<minDiff:
                    res=arr[l:r+1]
                    minDiff=currDiff
                currDiff-=abs(x-arr[l])
                l+=1
        
        return res