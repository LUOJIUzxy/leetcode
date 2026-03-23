
def backpack_01(weights, values, W):
     n = len(weights)
     # 初始化
     # 
     dp = [[0] * (W + 1) for _ in range(n + 1)]

     for i in range(1, n + 1):
          w = weights[i - 1]
          v = values[i - 1]
          # j 为背包剩余容量
          for j in range(W + 1):
               if j < w:
                    dp[i][j] = dp[i - 1][j]
               else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
          
     return dp[n][W]

weights = [1, 3, 4]
values = [15, 20, 30]
W = 4

print(backpack_01(weights, values, W))