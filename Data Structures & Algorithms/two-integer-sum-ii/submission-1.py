class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0, len(numbers)-1
        while l<r:
            diff=target-(numbers[l]+numbers[r])
            if diff==0:
                return [l+1,r+1]
            elif diff>0:
                l+=1
            else:
                r-=1
        
        return [-1,-1]