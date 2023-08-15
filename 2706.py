class Solution:
    def buyChoco(self, prices, money):
        x=min(prices)
        for i in range(len(prices)):
            if prices[i]==x:
                prices.pop(i)
                break
        y=min(prices)
        if x+y > money:
            return money
        else:
            return money-x-y