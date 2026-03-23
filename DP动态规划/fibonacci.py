
# 递归算法
def fib(n):
     if n <= 1:
          return n
     return fib(n - 1) + fib(n - 2)

# dp
def fib_dp(n):
     if n <= 1:
          return n
     
     # 牺牲空间复杂度，用一个array来存储 每一步骤的最佳结果
     dp = [0] * (n + 1)
     # 从数组下标1开始
     dp[0] = 0
     dp[1] = 1

     for i in range(2, n + 1):
          # 这里 dp[i] 就表示：第 i 个状态的答案。
          dp[i] = dp[i - 1] + dp[i - 2]

     return dp[n]