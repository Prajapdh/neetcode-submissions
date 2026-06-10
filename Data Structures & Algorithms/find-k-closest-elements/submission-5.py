class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Instead of having a index, we will perform binary search on a window
        l,r=0,len(arr)-k    #r isn't n-1 cause the index l and r are the start of the window
        while l<r:
            m=(r-l)//2+l
            # if the diff between x and first element in window is greater than the element after the window, we move towards right
            if x-arr[m]>arr[m+k]-x:
                l=m+1
            else:
                r=m

        return arr[l:l+k]