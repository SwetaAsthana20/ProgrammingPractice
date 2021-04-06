def maxProfit(prices) -> int:
    mini, maxi = prices[0], prices[0]
    temp = 0
    for i in prices:
        if i < mini:
            temp = temp if temp > maxi - mini else maxi - mini
            mini, maxi = i, i
        elif i > maxi:
            maxi = i
    return temp if temp > maxi - mini else maxi - mini


print(maxProfit([4, 16, 1, 4, 6, 19]))
