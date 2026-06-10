class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        l,r=0, n-1

        while r-l+1>k:
            print(l,r,k)
            # Since we need smaller number that is closest to x, we will only update l if diff is more
            if abs(x-arr[l])<=abs(x-arr[r]):
                r-=1
            else:
                l+=1

        return arr[l:r+1]