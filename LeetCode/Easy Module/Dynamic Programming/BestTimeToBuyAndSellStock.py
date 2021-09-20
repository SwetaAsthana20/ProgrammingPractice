def maxProfit(prices) -> int:
    mini, maxi = prices[0], prices[0]
    temp = 0
    for i in prices:
        if i < mini:
            mini, maxi = i, i
        elif i > maxi:
            maxi = i
        temp = temp if temp > maxi - mini else maxi - mini
    return temp


print(maxProfit([7,1,5,3,6,4]))
