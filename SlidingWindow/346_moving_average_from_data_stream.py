from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.window_sum = 0
        self.q = deque([])



    def next(self, val: int) -> float:
        self.q.append(val)
        self.window_sum += val

        if len(self.q) > self.size:
            removed = self.q.popleft()
            self.window_sum -= removed

        return self.window_sum / len(self.q)




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

movingAverage = MovingAverage(3)
print(movingAverage.next(1))# 返回 1.0 = 1 / 1
print(movingAverage.next(10)) # 返回 5.5 = (1 + 10) / 2
print(movingAverage.next(3)) #返回 4.66667 = (1 + 10 + 3) / 3
print(movingAverage.next(5)) # 返回 6.0 = (10 + 3 + 5) / 3