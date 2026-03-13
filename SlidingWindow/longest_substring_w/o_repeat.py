# slding widow + hash map
class Solution:
     def lengthOfLongestSubstring(self, s: str) -> int:
          if s is "":
               return 0
          result = 1
          l = 0
          r = 0
          umap = {}
          for r in range(len(s)):
               if s[r] in umap:
                    l = max(l, umap[s[r]] + 1)
               result = max(result, r-l+1)
               umap[s[r]] = r

          return result