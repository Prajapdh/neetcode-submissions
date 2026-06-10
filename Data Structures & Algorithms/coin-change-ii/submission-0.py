class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #Recursion
        # def dfs(i, amount):
        #     # print(i,coins[i], amount)
        #     if amount==0:
        #         return 1
        #     if i<0 or amount<0:
        #         return 0
        #     # Don't choose this coin
        #     # print("dont choose ", coins[i])
        #     res=dfs(i-1, amount)
        #     # Choose this coin
        #     if(coins[i]<=amount):
        #         # print("choose ", coins[i])
        #         res+=dfs(i, amount-coins[i])
        #     return res
        
        # return dfs(len(coins)-1, amount)
        
        # Memoization
        dp=[[-1]*(amount+1) for _ in range(len(coins))]
        # print(dp)
        def dfs(i, amount):
            if amount==0:
                return 1
            if i<0 or amount<0:
                return 0
            # print(i, amount)
            if dp[i][amount]!=-1:
                return dp[i][amount]

            # Don't choose this coin
            res=dfs(i-1, amount)
            # Choose this coin
            if(coins[i]<=amount):
                res+=dfs(i, amount-coins[i])
            dp[i][amount]=res
            return res
        return dfs(len(coins)-1, amount)