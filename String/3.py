# LeetCode 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# 滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n
        
        # unique , 不重复
        visited = set()
        l = 0
        r = 1
        res = 1

        while l <= r and r < n:
            if s[r] in visited:
                visited.remove(s[l])
                l += 1
            else:
                visited.add(s[r])
                r += 1
                res = max(res, r - l +1)
        return res
