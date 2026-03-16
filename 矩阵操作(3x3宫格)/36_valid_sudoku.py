from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows(i) -> 包含哪些元素
        # cols(i) -> 包含哪些元素
        # boxes(i) i = 1~9 -> 包含哪些元素

        # 检查是否有重复（去重），用set，查找速度快

        for i in range(9):
            row = board[i]
            row_pure = [x for x in row if x != "."]
            row_set = set(row_pure)

            if len(row_pure) != len(row_set):
                return False
            
            col = []
            for j in range(9):
                col.append(board[j][i])
            col_pure = [x for x in col if x != "."]
            col_set = set(col_pure)

            if len(col_pure) != len(col_set):
                return False


            box_row = i // 3
            box_col = i % 3
            box = []
            for m in range(3):
                for n in range(3):
                    box.append(board[box_row * 3 + m][box_col * 3 + n])
            
            box_pure = [x for x in box if x != "."]
            box_set = set(box_pure)
            if len(box_pure) != len(box_set):
                return False

        return True

            
