class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0 for num in range(amount + 1)]
        
        for num in range(1,amount + 1):
            mn = float("inf")
            for coin in coins:
                if coin > num:
                    continue
                mn = min(mn, 1 + dp[num-coin])
            dp[num] = mn
        print(dp)
        
        return dp[amount] if dp[amount] != float("inf") else -1
