class Solution:
    def merge(self, arr1, arr2):
            i=j=0
            res=[]
            while i<len(arr1) and j<len(arr2):
                if arr1[i]<arr2[j]:
                    res.append(arr1[i])
                    i+=1
                else:
                    res.append(arr2[j])
                    j+=1
            res+= arr1[i:] if i<len(arr1) else arr2[j:]
            return res

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        half = len(nums)//2
        # print(nums, nums[:half], nums[half:])
        return self.merge(self.sortArray(nums[:half]), self.sortArray(nums[half:]))
        