class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # if a number occurs more than half amount of time, it is the most occured element
        count = res = 0

        for num in nums:
            # If the last element wasnt most occured, set a new one
            if count == 0:
                res=num
            
            count += (1 if res==num else -1)    #Solution always exists, most occured element will have +ve coutn at end
        return res
            