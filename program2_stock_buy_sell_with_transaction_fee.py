"""
Experiment 10: Shortest Paths
Program 2: Stock Buy/Sell with Transaction Fee
Aim: Maximize stock trading profit with a fixed transaction fee.
"""

def max_profit(prices, fee):
    cash, hold = 0, -prices[0]
    for price in prices[1:]:
        old_cash = cash
        cash = max(cash, hold + price - fee)
        hold = max(hold, old_cash - price)
    return cash

print(max_profit([1, 3, 2, 8, 4, 9], 2))
