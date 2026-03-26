from typing import List

class Solution:
    def distribute_stones(self, extra: List[List[int]], empties: List[List[int]]):
        # len(extra) == len(empties)
        for i in range(len(extra)):
            move = abs(extra[i][0] - empties[i][0]) + abs(extra[i][1] - empties[i][1])

    


    def minimumMoves(self, grid: List[List[int]]) -> int:
        extra = [[]]
        empties = [[]]
        for i in range(3):
            for j in range(3):
                if grid[i][j] > 1:
                    # 相当于是有多余的几个stone，就append几次
                    for _ in range(grid[i][j] - 1):
                        extra.append([i, j])
                if grid[i][j] == 0:
                    empties.append([i, j])

                
        
        