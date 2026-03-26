import sys


def recursive(empty: int, result: int) -> int:
     coke = empty // 3
     result += coke
     left = empty % 3 + coke
     if empty < 3:
          if left == 2:
               return result + 1
          else:
               return result
    


     print((left, result))
     return recursive(left, result)


for line in sys.stdin:
    a = line.split()

    result = 0
    true_result = recursive(int(a[0]), result)
    if true_result == 0:
         print(None)
    print(true_result)

    
    

