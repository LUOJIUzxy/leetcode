class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
          result = 0
          s = set(nums)

          for i in s:
               if i - 1 not in s:   # i 是连续序列起点
                    current = i
                    while current + 1 in s:
                         current += 1
                    result = max(result, current - i + 1)

          return result