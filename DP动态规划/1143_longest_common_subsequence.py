
def longestCommonSubsequence(text1: str, text2: str) -> int:
     n = len(text1)
     m = len(text2)

     # dp[i][j] 表示 text1[0:i] 和 text2[0:j] 的 LCS 长度
     dp = [[0] * (m + 1) for _ in range(n + 1)]

     for i in range(1, n + 1):
          for j in range(1, m + 1):
               if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
               #含义： 当前字符不匹配，所以 LCS 长度要从两个子问题中取较大值：
# dp[i-1][j] → 跳过 text1 的当前字符，把text2的“指针”往后滑动一位，用 text1[0:i-1] 和 text2[0:j] 的 LCS
# dp[i][j-1] → 跳过 text2 的当前字符，把text1的“指针”往后滑动一位，用 text1[0:i] 和 text2[0:j-1] 的 LCS
               else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

     return dp[n][m]

print(longestCommonSubsequence("abcde", "ace"))