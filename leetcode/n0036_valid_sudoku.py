from typing import (
    Any,
    DefaultDict,
    Dict,
    Iterator,
    List,
    NamedTuple,
    Optional,
    Set,
    Union,
)
from bisect import (
    bisect_left,
    bisect_right,
)
from itertools import (
    accumulate,
    chain,
    cycle,
    islice,
    permutations,
    product,
    repeat,
    takewhile,
)
from functools import (
    cached_property,
)
from collections import (
    defaultdict,
    deque,
)


class ListNode:
    def __init__(
            self,
            x: int,
            next: Optional['ListNode'] = None,
    ):
        self.val: int = x
        self.next: 'ListNode' = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: 'TreeNode' = None,
        right: 'TreeNode' = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Position(NamedTuple):
    x: int
    y: int


class Board:

    rows: DefaultDict[int, DefaultDict[str, int]]
    # rows[n] represents how many particular character appeared in the (n+1)th row

    columns: DefaultDict[int, DefaultDict[str, int]]
    # columns[n] represents how many particular character appeared in the (n+1)th column

    sub_boards: DefaultDict[Position, DefaultDict[str, int]]
    # 0 <= i, j <= 2
    # sub_board[i][j] represents how many particular character appear in the i-th row and j-th column

    def is_valid(self) -> bool:

        def check(dict_: DefaultDict[Any, Dict]) -> bool:
            return all(
                value > 0
                for values in dict_.values()
                for value in values
            )

        valid_rows = check(dict_=self.rows)
        valid_columns = check(dict_=self.columns)
        valid_sub_boards = check(dict_=self.sub_boards)

        return (
            valid_rows and
            valid_columns and
            valid_sub_boards
        )

    def add_cell(
        self,
        position: Position,
        value: str,
    ):
        if value != ".":
            self.rows[position.x][value] += 1
            self.columns[position.y][value] += 1

            sub_board_position = Position(
                x=position.x // 3,
                y=position.y // 3,
            )
            self.sub_boards[sub_board_position][value] += 1

    def __init__(self):
        self.rows = defaultdict(lambda: defaultdict(lambda: 0))
        self.columns = defaultdict(lambda: defaultdict(lambda: 0))
        self.sub_boards = defaultdict(lambda: defaultdict(lambda: 0))


class Solution:

    def isValidSudoku(
        self,
        board: List[List[str]],
    ) -> bool:

        board_ = Board()

        for x, y in product(
            range(9),
            range(9),
        ):
            board_.add_cell(
                position=Position(x=x, y=y),
                value=board[x][y],
            )

        return board_.is_valid()


if __name__ == '__main__':
    solution = Solution()
    for board in [
        # [
        #     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
        #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
        #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        #     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        # ],
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    ]:
        print(
            solution.isValidSudoku(board=board)
        )
