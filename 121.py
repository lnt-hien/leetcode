def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    min_purchase = float('inf')
    for price in prices:
        min_purchase = min(min_purchase, price)
        max_profit = max(max_profit, price - min_purchase)
                
    return max_profit