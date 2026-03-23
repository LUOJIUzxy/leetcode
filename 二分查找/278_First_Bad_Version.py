# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
    
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        mid = left + (right - left) // 2 

        # use binary search
        while mid >= 1:
            mid = left + (right - left) // 2 
            if right - left <= 1:
                if isBadVersion(left) == False:
                    return right
                else: 
                    return left

            if isBadVersion(mid) == True:
                right = mid
                if isBadVersion(left) == False:
                    continue
                else:
                    return left
            else:
                left = mid
                if isBadVersion(right) == True:
                    continue
                else:
                    return right
        