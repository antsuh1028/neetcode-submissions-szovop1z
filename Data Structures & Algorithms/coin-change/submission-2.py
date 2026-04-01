class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for num in range(amount + 1)]
        dp[0] = 0
    
        
        for num in range(1,amount + 1):
            for coin in coins:
                if coin > num:
                    continue
                dp[num] = min(dp[num], 1 + dp[num-coin])
            
        print(dp)
        
        return dp[amount] if dp[amount] != float("inf") else -1
