from typing import List
from collections import defaultdict
from itertools import product


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        sub_boxes = defaultdict(set)

        for i, j in product(range(9), range(9)):
            square = board[i][j]
            if square == ".":
                continue
            if square in rows[i]:
                return False
            if square in columns[j]:
                return False
            sub_box_id = (i // 3, j // 3)
            if square in sub_boxes[sub_box_id]:
                return False

            rows[i].add(square)
            columns[j].add(square)
            sub_boxes[sub_box_id].add(square)

        return True


if __name__ == "__main__":
    s = Solution()
    board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
             ["4", ".", ".", "5", ".", ".", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", ".", "3"],
             ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
             [".", ".", ".", "8", ".", "3", ".", ".", "5"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", ".", ".", ".", ".", ".", "2", ".", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "8"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    result = s.isValidSudoku(board=board)
    print(result)
