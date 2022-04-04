# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# easier to understand with a picture

def maxProfit(prices) -> int:
        
    left, right = 0, 1
    maxP = 0
    while right < len(prices):
        
        # if the price on the left is lower then save that profit
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxP = max(profit, maxP)
        else:
            # if the right is lower then move the left to that spot
            left = right
        right += 1
    
    return maxP