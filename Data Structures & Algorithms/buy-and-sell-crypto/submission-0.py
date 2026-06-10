class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        startPos=0
        for i, p in enumerate(prices):
            if(p<prices[startPos]):
                startPos=i
            else:
                profit = p-prices[startPos]
                maxProfit=max(maxProfit, profit)
        
        return maxProfit