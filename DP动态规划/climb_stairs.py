
# 一共有n阶, 每次跨1 / 2阶梯，求最终到达的方法数目
def climbStairs(n: int) -> int:
     if n <= 2:
          return n
     
     dp = [0] * (n + 1)
     dp[1] = 1
     dp[2] = 2

     for i in range(3, n + 1):
          dp[i] = dp[i - 1] + dp[i - 2]

     return dp[n]

n = 8
print(climbStairs(n))