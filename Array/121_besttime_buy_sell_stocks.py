import math
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 遍历一遍，拿到每一天当天价格卖出能获得的最大盈利
        max_daily_profit = 0

        # 如何获取当天的最大盈利，记录并更新最低的买点
        min_num = math.inf
        for i, price in enumerate(prices):
            if min_num > price:
                min_num = price
            
            max_daily_profit = max(max_daily_profit, price - min_num)

        return max_daily_profit


        