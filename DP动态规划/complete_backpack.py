# 关键就在“选这个物品之后，后面还能不能继续选它”。
# 选了第 i 个物品一次后，还可以继续选，所以看的是：
# dp[i][j - w] + v

# 注意这里是 i，不是 i-1。

# 这非常关键。

def backpack_complete(weights, values, W):
     n = len(weights)
     dp = [[0] * (W + 1) for _ in range(n + 1)]

     for i in range(1, n + 1):
          weight = weights[i - 1]
          value = values[i - 1]

          for j in range(W + 1):
               if j < weight:
                    dp[i][j] = dp[i - 1][j]
               else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - weight] + value)

     return dp[n][W]

weights = [1, 3, 4]
values = [15, 20, 30]
W = 4

print(backpack_complete(weights, values, W))