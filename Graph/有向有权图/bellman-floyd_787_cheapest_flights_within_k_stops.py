import math
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [math.inf] * n
        dist[src] = 0

        # 这里限制了egdes只能往后拓展 k+1 次， 因为从str起始点开始
        for i in range(k + 1):
            temp = dist[:]
            # 这一层循环是把一个节点的所有next节点全部遍历出来
            for flight in flights:
                _from = flight[0]
                to = flight[1]
                price = flight[2]
                if dist[_from] != math.inf:
                    # 使用temp，防止前面某条边刚把 dist[u] 更新了，后面另一条边马上又拿这个“刚更新的新值”继续更新别的点
                    # 保证i这一轮只会拓展一条边
                    # temp[to] 保存本i轮目前为止到 to的最好结果
                    
                    # 读旧表，写新表，但新表自己要累积最优值
                    temp[to] = min(temp[to], dist[_from] + price)
                
            dist = temp
        
        return -1 if dist[dst] == math.inf else dist[dst]

        