class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.prefixSum=[0]
        for i in range(len(nums)):
            self.prefixSum.append(self.prefixSum[-1]+nums[i])
        print(self.prefixSum)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right+1]-self.prefixSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)