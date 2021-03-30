from typing import List


def maxProfit(prices: List) -> int:
    size = len(prices)
    buy = -1  # Flag to identify whether we have bought the stocks yet or not.
    profit = 0  # Total profit gain

    for i in range(0, size):
        if buy == -1:  # No stocks bought yet, can buy new one.
            if i != size - 1 and prices[i] < prices[i + 1]:  # i!= size-1 because we don't want to buy at the last day
                buy = prices[i]

        elif buy != -1:
            if i == size - 1 or prices[i] > prices[i + 1]:  # we have to sell the stock at last day at any cost.
                profit += prices[i] - buy
                buy = -1

    return profit


print(maxProfit([7, 1, 5, 6, 3, 0, 9]))
