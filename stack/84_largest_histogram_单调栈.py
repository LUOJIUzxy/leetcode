from typing import List

from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = deque([0])
        rectangle = 0
        h = 0

        for i, height in enumerate(heights[1:], start=1):
            top = stack[-1]

            while height < heights[top]:
                right = i
                
                if stack:
                    old_top = stack.pop()
                    h = heights[old_top]
                    if stack:
                        top = stack[-1]
                        left = top
                    else:
                        left = -1
                        rectangle = max(rectangle, h * (right - left - 1))
                        break
                rectangle = max(rectangle, h * (right - left - 1))
            
            stack.append(i)

            
        
        return rectangle
            

## TLE or MLE        
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights_set = set(heights)

        rectangle_max = []
        for height in heights_set:
            length = 0
            rec_max = 0
            for histogram in heights:
                
                if height > histogram:
                        rec_max = max(rec_max, length * height)
                        length = 0
                else:
                        length += 1

            if length != 0:
                rec_max = max(rec_max, length * height)

            rectangle_max.append(rec_max)

        
        return max(rectangle_max)
            

        