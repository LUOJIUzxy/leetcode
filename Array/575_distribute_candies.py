from typing import List


# def distributeCandies(candyType: List[int]) -> int:
#      candie_type_set = set(candyType)
#      candie_quantity = len(candyType) // 2
#      if candie_quantity <= len(candie_type_set):
#           return candie_quantity
#      else: 
#           return len(candie_type_set)

def distributeCandies(candyType: List[int]) -> int:
     
     return min(len(candyType) // 2, len(set(candyType)))

print(distributeCandies([1,1,2,2,3,3]))
print(distributeCandies([1,1,2,3]))
print(distributeCandies([6,6,6,6]))
        