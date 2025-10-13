class Solution(object):
    def maxProfit(self, prices):
        max_price = 0
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                cur_price = price - min_price
                max_price = max(max_price, cur_price)
        return max_price
            

        