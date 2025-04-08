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
