from typing import List

# worst case: o(n^2)
def solution(nums: List[int]) -> int:

     nums_set = set(nums)
     length_sequence = [1] * len(nums)
     for i, num in enumerate(nums):
          while num + 1 in nums_set:
               length_sequence[i] += 1
               num += 1
     
     return max(length_sequence)

# o(n)
def longestConsecutive(self, nums: List[int]) -> int:

        result = 0
        s = set(nums)
        for i in s:
            if i-1 not in s: # o(1)
                #find the consecutive sequence start point

                current = i
                while current + 1 in s:
                    current += 1
                result = max(result, current - i + 1)
        
        return result


nums = [0,3,7,2,5,8,4,6,0,1]
print(solution(nums))