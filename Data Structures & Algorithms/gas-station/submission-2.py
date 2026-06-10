class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # First check if the solution exists: there is enough fuel to cover all costs
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            # add the difference at index i to the total
            total += (gas[i] - cost[i])

            # if the total dips below 0, we can't mover forward from that position
            if total < 0:
                total = 0
                res = i + 1
        
        return res