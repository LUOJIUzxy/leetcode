def dfs(grid, r, c):
     rows, cols = len(grid), len(grid[0])

     if r < 0 or r >= rows or c < 0 or c >= cols:
        return
     
     if grid[r][c] != "1":
         return

     grid[r][c] = "0" # marked as visited

     # 上下左右
     dfs(grid, r - 1, c)
     dfs(grid, r + 1, c)
     dfs(grid, r, c - 1)
     dfs(grid, r, c + 1)

def numIslands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                dfs(grid, r, c)
                count += 1

    return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))