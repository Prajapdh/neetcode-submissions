class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # using backtracking
        # T.C: n!*n  (n! becasue we have n,n-1,n-2.. choices)(n because we go through array to check if the element was added or not and then add it)

        res=[]
        perm=[]

        def backtrack(perm, pick):
            print(perm)
            if(len(perm)==len(nums)):
                res.append(perm.copy()) # adding a copy because we want all answers, since we are backtracking single perm is used
                return

            for i in range(len(nums)):
                # adding an element to perm if it doesn't exist
                if not pick[i]:
                    pick[i]=True
                    perm.append(nums[i])
                    backtrack(perm, pick)
                    # Cleaning to backtrack
                    perm.pop()
                    pick[i]=False


        backtrack(perm, [False]*len(nums))
        return res