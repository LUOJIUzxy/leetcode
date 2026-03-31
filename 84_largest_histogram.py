from typing import List

def largestRectangleArea(heights: List[int]) -> int:
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

heights = [2, 0, 2]
print(largestRectangleArea(heights))      

        