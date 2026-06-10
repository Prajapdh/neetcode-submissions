class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        l,r=0,n-1
        while l<r:
            if (r-l)//2<=k:
                # print(arr[l:r+1])
                # Perform linear search
                while r-l+1>k:
                    if abs(arr[l]-x)<=abs(arr[r]-x):
                        r-=1
                    else:
                        l+=1
                return arr[l:r+1]
            else:
                mid=(r-l)//2+l
                # print(l,l+mid//2,r-mid//2,r)
                if abs(arr[r-mid//2]-x)<=abs(arr[l+mid//2]-x):
                    l+=mid//2
                else:
                    r-=mid//2
        return []