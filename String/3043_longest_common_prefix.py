from typing import List
# from math import log10

def longestCommonPrefix(arr1: List[int], arr2: List[int]) -> int:
     prefix_arr1 = set() # {}


     for arr in arr1:
          # int(log10(arr)) + 1
          for i in range(1, len(str(arr)) + 1):
               prefix_arr1.add(str(arr)[:i])
          
     max_result = 0
     for arr in arr2:
          count = 0
          for i in range(1, len(str(arr)) + 1):
               if str(arr)[:i] in prefix_arr1:
                   count += 1
                   # 876543
               else:
                   break
          max_result = max(count, max_result)
     
     return max_result

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        prefix_arr1 = set() # {}

        for arr in arr1:
            # int(log10(arr)) + 1
            sub_arr = arr
            while sub_arr != 0:
                prefix_arr1.add(sub_arr)
                sub_arr = sub_arr // 10
                
            # for i in range(1, len(str(arr)) + 1):
            #     prefix_arr1.add(str(arr)[:i])
            
        max_result = 0
        for arr in arr2:
            count = 0
            sub_arr = arr
            while sub_arr != 0:
                if sub_arr in prefix_arr1:
                    count += 1
                sub_arr = sub_arr // 10
            # for i in range(1, len(str(arr)) + 1):
            #     if str(arr)[:i] in prefix_arr1:
            #         count += 1
            #         # 876543
            #     else:
            #         break
            max_result = max(count, max_result)
        
        return max_result

arr1 = [1,10,100]
arr2 = [1000]
print(longestCommonPrefix(arr1, arr2))          
          
          



