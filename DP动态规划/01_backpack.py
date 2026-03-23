
def backpack_01(weights, values, W):
     n = len(weights)
     # 初始化
     # 
     dp = [[0] * (W + 1) for _ in range(n + 1)]

     for i in range(1, n + 1):
          w = weights[i - 1] #按照数组下标，当前的weight
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

# 01 背包的一维优化

# 二维 DP 很好理解，但空间是 O(nW)。
# 其实每一行只依赖上一行，所以可以压缩成一维。

def knapsack_01(weights, values, W):
    dp = [0] * (W + 1)

    for i in range(len(weights)):
        w = weights[i]
        v = values[i]
        for j in range(W, w - 1, -1):   # 倒序
            dp[j] = max(dp[j], dp[j - w] + v)

    return dp[W]