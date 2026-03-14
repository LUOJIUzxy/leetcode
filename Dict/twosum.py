class solution:
     def twoSum(self, nums, target):
          # visited里面存储数值 -> 下标
          visited = {}
          for i, num in enumerate(nums):
               need = target - num
               if need in visited.keys():
                    return [i, visited[need]]
               visited[num] = i
