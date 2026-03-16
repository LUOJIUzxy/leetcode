from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
     rows, cols = len(heights), len(heights[0])
     results = []


     def dfs_pacific(r, c, visited) -> bool:
          if r < 0 or r >=rows or c < 0 or c >= cols:
               return False
          
          # (r, c) is visited
          if (r, c) in visited:
               return False
          # if heights[r][c] < heights[r-1][c] or heights[r][c] < heights[r+1][c] or heights[r][c] < heights[r][c-1] or heights[r][c] < heights[r][c+1]:
          #     return False
          if r == 0 or c == 0:
               return True
          
          visited.add((r, c))

          

          directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
          for dr, dc in directions:
               nr, nc = r + dr, c + dc
               if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] <= heights[r][c]:
                    if dfs_pacific(nr, nc, visited):
                         return True
          return False
     
     def dfs_atlantic(r, c, visited) -> bool:
          if r < 0 or r >=rows or c < 0 or c >= cols:
               return False
     
          if (r, c) in visited:
               return False

          if r == rows - 1 or c == cols - 1:
               return True
          visited.add((r, c))

          # (r, c) is visited
          directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
          for dr, dc in directions:
               nr, nc = r + dr, c + dc
               if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] <= heights[r][c]:
                    if dfs_atlantic(nr, nc, visited):
                         return True
          return False



     # 双层循环遍历每一个点，然后用dfs快速探查到最低点，看能不能到边（把整块淹没掉）
     for i in range(rows):
          for j in range(cols):
               visited_1 = set()
               visited_2 = set()
               if dfs_pacific(i, j, visited_1) and dfs_atlantic(i, j, visited_2):
                    results.append([i, j])

     return results
        

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacificAtlantic(heights))
