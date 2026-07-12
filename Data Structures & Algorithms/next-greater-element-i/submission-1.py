class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # monotonically decreasing stack
        stack=[]    #sotres indices
        nextGreater=[-1]*len(nums2)
        idxMap={}
        for i, num in enumerate(nums2):
            while stack and nums2[stack[-1]]<num:
                nextGreater[stack.pop()]=num
            stack.append(i)
            idxMap[num]=i
        res=[]
        for num in nums1:
            res.append(nextGreater[idxMap[num]])
        
        return res