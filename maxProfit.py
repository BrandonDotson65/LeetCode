def maxProfit(pricesList):
    maxProfit = 0
    minprice = float('inf')
    for price in pricesList:
        minprice = min(minprice, price)
        profit = price - minprice
        maxProfit = max(maxProfit, profit)
    return maxProfit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))