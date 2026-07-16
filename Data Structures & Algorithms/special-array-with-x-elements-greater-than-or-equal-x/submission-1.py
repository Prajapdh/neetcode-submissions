class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n=len(nums)
        # Store the count of numbers greater than current number
        counter=[0]*(n+1)   # max possible value of x is len(nums)
        for num in nums:
            if num>=n:
                counter[n]+=1   # Increment the count of n if we see any element greater than equal to n
            else:
                counter[num]+=1

        greaterElements=0
        for i in range(n, 0, -1):
            greaterElements+=counter[i] # Number of elements greater than or equal to i. It acts like a suffix for counter
            # there are exactly i elements greater than equal to i
            if greaterElements==i:
                return i
        
        return -1