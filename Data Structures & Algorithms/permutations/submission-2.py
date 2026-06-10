class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time: n!*n*n (we need n!*n to find permutations and insert 1 number, we need to insert n numbers)
        # Base case
        if len(nums)==0:
            return [[]]
        
        # skip the first element and make permutations for rest of the array
        perms=self.permute(nums[1:])
        res=[]
        # now lets add our first element in all indices for all permutation we got
        for p in perms:
            for i in range(len(p)+1):
                # we don't want to change the permutation as we have to add first element at different indices
                pCopy=p.copy()
                pCopy.insert(i, nums[0])
                res.append(pCopy)
        # res is new set of permutations including the first element
        return res