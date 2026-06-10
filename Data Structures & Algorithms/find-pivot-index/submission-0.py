class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # if prefixSum[i]==suffixSum then return i, else -1
        n=len(nums)
        prefixSum=[0 for _ in range(n)]
        suffixSum=[0 for _ in range(n)]
        # calculate prefixSum and suffixSum
        for i in range(1,n):
            prefixSum[i]=prefixSum[i-1]+nums[i-1]
            suffixSum[n-1-i]=suffixSum[n-i]+nums[n-i]
        # print(prefixSum)
        # print(suffixSum)
        for i in range(n):
            if prefixSum[i]==suffixSum[i]:
                return i

        return -1