from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visited = [[False] * cols for _ in range(rows)]
            q = deque(starts)

            for r, c in starts:
                visited[r][c] = True

            while q:
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        not visited[nr][nc] and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        visited[nr][nc] = True
                        q.append((nr, nc))

            return visited

        pacific = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        pac = bfs(pacific)
        atl = bfs(atlantic)

        return [[r, c] for r in range(rows) for c in range(cols) if pac[r][c] and atl[r][c]]
