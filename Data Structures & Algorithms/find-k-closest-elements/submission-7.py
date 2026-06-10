class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r>l:
            mid=(r-l)//2+l
            if(mid+k<len(arr) and abs(x-arr[mid])>abs(x-arr[mid+k])):
                l=mid+1
            else:
                r=mid

        return arr[l: l+k]