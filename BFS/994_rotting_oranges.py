from collections import deque
from typing import List

# starts = [(i, j), (i, j)] 
def bfs(starts: List, grid: List[List[int]], fresh_num: int):
     R = len(grid)
     C = len(grid[0])
     q = deque()
     # visited = set()
     for start in starts:
          # start = (i, j)
          q.append(start)
          
     level = 0

     infected_nums = 0

     while q and infected_nums < fresh_num:
          # node = (r, c)
          
          current_nodes = q
          q = deque()
          for (r, c) in current_nodes:
               directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
               for nr, nc in directions:
                    lr = r + nr
                    lc = c + nc 
                    if 0 <= lr < R and 0 <= lc < C and grid[lr][lc] == 1:
                         grid[lr][lc] = 2
                         infected_nums += 1
                         q.append((lr, lc))
                         
          
          level += 1

     return infected_nums, level


def orangeRotting(grid: List[List[int]]) -> int:
     # 找出所有的start，表示grid中有这么多个连通块，全部跑一遍bfs，看能不能跑完所有（1->2). 能的话，记录下来 max(level)
     m = len(grid[0])
     n = len(grid)
     starts = []
     fresh_nums = 0

     for i in range(n):
          for j in range(m):
               if grid[i][j] == 2:
                    starts.append((i, j))
               elif grid[i][j] == 1:
                    fresh_nums += 1

     infected_num, level = bfs(starts, grid, fresh_nums)

     if infected_num < fresh_nums:
          return -1
     else:
          return level
     
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangeRotting(grid))

