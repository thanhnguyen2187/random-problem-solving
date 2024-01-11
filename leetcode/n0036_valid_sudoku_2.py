from typing import (
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
    combinations,
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
    Counter,
)


def get_subbox(board: List[List[str]], x: int, y: int) -> List[str]:
    x_range = (3 * x, 3 * (x + 1))
    y_range = (3 * y, 3 * (y + 1))
    rows = [
        row[x_range[0]:x_range[1]]
        for row in board[y_range[0]:y_range[1]]
    ]
    result = [
        *rows[0],
        *rows[1],
        *rows[2],
    ]
    return result


def get_row(board: List[List[str]], y: int) -> List[str]:
    return [
        cell
        for cell in board[y]
    ]


def get_column(board: List[List[str]], x: int) -> List[str]:
    return [
        board[y][x]
        for y in range(0, 9)
    ]


valid_characters = {
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9",
    "."
}


def is_valid_list(list_: List[str]) -> bool:
    for item in list_:
        if item not in valid_characters:
            return False
    counter = Counter(list_)
    counter["."] = 0
    return len([
        count
        for count in counter.values()
        if count >= 2
    ]) == 0


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subboxes = [
            get_subbox(board=board, x=x, y=y)
            for x, y in product(range(0, 3), range(0, 3))
        ]
        for subbox in subboxes:
            if not is_valid_list(list_=subbox):
                return False

        rows = [
            get_row(board=board, y=y)
            for y in range(0, 9)
        ]
        for row in rows:
            if not is_valid_list(list_=row):
                return False

        columns = [
            get_column(board=board, x=x)
            for x in range(0, 9)
        ]
        for column in columns:
            if not is_valid_list(list_=column):
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    # print(get_subbox(board=board, x=2, y=2))
    # print(get_row(board=board, y=2))
    # print(get_column(board=board, x=1))
    # print(is_valid_list(list_=["1", "2", "3", "."]))
    # print(is_valid_list(list_=["1", "2", "3", "1"]))
    print(solution.isValidSudoku(board=board))
