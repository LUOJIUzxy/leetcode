from typing import List
from math import inf

def maxProfit(prices: List[int]) -> int :
     result = 0
     min_buy = inf

     for price in prices:
          min_buy = min(min_buy, price)
          result = max(result, price - min_buy)

     return result

def maxProfit(self, prices: List[int]) -> int:
        # 遍历一遍，拿到每一天当天价格卖出能获得的最大盈利
        max_daily_profit = 0

        # 如何获取当天的最大盈利，记录并更新最低的买点
        min_num = inf
        for i, price in enumerate(prices):
            if min_num > price:
                min_num = price
            
            max_daily_profit = max(max_daily_profit, price - min_num)

        return max_daily_profit

prices = [7, 1, 3, 2, 5, 6, 4]
print(maxProfit(prices))