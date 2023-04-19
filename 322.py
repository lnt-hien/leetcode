# Bottom-up DP (Tabulation)
def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
                print(dp)
        
    return dp[amount] if dp[amount] != amount + 1 else -1 


# Top-down DP(Memoization)
def coinChange(self, coins: List[int], amount: int) -> int:            
    def coinChangeInner(rem, cache):
        if rem < 0:
            return math.inf
        if rem == 0:                    
            return 0       
        if rem in cache:
            return cache[rem]
        
        cache[rem] = min(coinChangeInner(rem-x, cache) + 1 for x in coins)                         
        return cache[rem]      
    
    ans = coinChangeInner(amount, {})
    return -1 if ans == math.inf else ans                