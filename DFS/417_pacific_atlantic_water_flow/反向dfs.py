from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        # define 两边的从边能向内扩散访问的路径图集合set， 最后求两个set的交集
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            
            # set里面存二元组的形式
            visited.add((r, c))

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for (dr, dc) in directions:
                nr, nc = r + dr, c + dc 
                # ensure not list out of range
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        # pacific: (0, c), (r, 0)
        for c in range(cols):
            dfs(0, c, pacific)
        for r in range(rows):
            dfs(r, 0, pacific)

        #atlantic: (rows - 1, c), (r, cols - 1)
        for c in range(cols):
            dfs(rows - 1, c, atlantic)
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        results_set = pacific & atlantic
        results = []
        for tuple_point in results_set:
            results.append(list(tuple_point))
        return results
            
