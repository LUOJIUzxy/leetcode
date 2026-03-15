from collections import deque

def bfs_grid(grid, r, c):
     rows, cols = len(grid), len(grid[0])

     q = deque([(r, c)])
     grid[r][c] = "0"

     while q:
          (x, y) = q.popleft()

          for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
               nx ,ny = x + dx, y + dy

               if 0 <= nx <= rows and 0 <= ny <= cols and grid[nx][ny] == "1":
                    q.append((nx, ny))
                    grid[nx][ny] = "0"