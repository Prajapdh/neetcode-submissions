class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Brute Force. ON: (n*2^n), SN: (n*2^n)
        res=[]
        candidates.sort()   # answers will always be in sorted order
        print(candidates)
        def dfs(i, curr, total):
            # print(f"i: {i}, curr: {curr}")
            if(total==target):
                res.append(curr.copy())
                return
            if(i>=len(candidates) or total>target):
                return
            
            
            curr.append(candidates[i])
            dfs(i+1, curr, total+candidates[i])
            curr.pop()
            
            # if we don't want to choose the ith value, skip the duplicates of ith value
            while(i<(len(candidates)-1) and (candidates[i+1]==candidates[i])):
                i+=1
            dfs(i+1, curr, total)

        dfs(0, [], 0)
        return res