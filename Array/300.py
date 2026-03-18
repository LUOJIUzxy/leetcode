# 300. 最长递增子序列
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度

# 示例 1：
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 示例 2：
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 解释：最长递增子序列是 [0,1,2,3]，因此长度为 4 。
# 示例 3：
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1   
# 解释：最长递增子序列是 [7]，因此长度为 1 。
# 提示：
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
# 进阶：
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗？

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        # dp[i] 表示：以 nums[i] 这个元素结尾的最长递增子序列的长度

        for i in range(len(nums)):
            for j in range(i):
                # 从下标 j=0 遍历到 j=i-1，检查能否在 nums[j] 后面接上 nums[i]
                if nums[j] < nums[i]:
                    # 如果 nums[i] > nums[j]，则可以把 nums[i] 连接到
                    # “以 nums[j] 结尾的递增子序列”之后
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            idx = bisect.bisect_left(tails, num)

            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num

        return len(tails)
