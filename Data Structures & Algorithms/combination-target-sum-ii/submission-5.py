class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def dfs(i, curr, currSum):
            if currSum==target:
                res.append(curr.copy()) # takes n complexity to copy list 
                return
            if i>=len(candidates) or currSum>target:
                return
            
            curr.append(candidates[i])
            dfs(i+1, curr, currSum+candidates[i])
            curr.pop()
            # If we have decided to skip this ele, skip all occ of that ele
            while i+1<len(candidates) and candidates[i+1]==candidates[i]:
                i+=1
            dfs(i+1, curr, currSum)
        dfs(0, [], 0)
        return res