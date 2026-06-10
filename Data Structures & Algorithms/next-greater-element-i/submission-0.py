class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # use a monotonically decreaing stack
        stack=[]    #stores index
        nextGreater=[-1]*len(nums2) #stores value of next greater ele
        # for each ele we check top of stack, if curr ele is greater than top of stack, we pop it and set it in helper array
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]]<nums2[i]:
                nextGreater[stack[-1]]=nums2[i]
                stack.pop()
            stack.append(i)
        
        nums2Map={}
        for i,n in enumerate(nums2):
            nums2Map[n]=i
        
        res=[]
        for n in nums1:
            res.append(nextGreater[nums2Map[n]])
        
        return res
