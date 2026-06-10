class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        left,right=0,0
        window={}
        for right in range(len(nums)):   
            window[nums[right]] = 1 + window.get(nums[right],0)
            print(f"window: {window}")
            lenn=right-left+1
            if(lenn==k):
                print(left, right)
                
                res.append(max(window))
                print(f"l: {left}, n: {nums[left]}")
                window[nums[left]]-=1
                if(window[nums[left]]==0): del window[nums[left]]
                left+=1
            
        return res