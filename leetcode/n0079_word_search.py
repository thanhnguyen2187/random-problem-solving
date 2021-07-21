from typing import (
    List,
    NamedTuple,
)
from itertools import (
    product,
)


class Cell(NamedTuple):
    x: int
    y: int
    character: str


class Solution:

    def attempt(
        self,
        board: List[List[str]],
        marks: List[List[bool]],
        width: int,
        height: int,
        word: str,
        depth: int,
        current_cell: Cell,
    ):
        if current_cell.character != word[depth]:
            return False
        elif depth == len(word) - 1 and current_cell.character == word[depth]:
            return True

        marks[current_cell.y][current_cell.x] = True
        possible = (
            self.attempt(
                board=board,
                marks=marks,
                width=width,
                height=height,
                word=word,
                depth=depth + 1,
                current_cell=adjacent_cell,
            )
            for adjacent_cell in [
                Cell(x=x, y=y, character=board[y][x])
                for x, y in [
                    (current_cell.x + 1, current_cell.y),
                    (current_cell.x - 1, current_cell.y),
                    (current_cell.x, current_cell.y + 1),
                    (current_cell.x, current_cell.y - 1),
                ]
                if (
                    (0 <= x < width) and
                    (0 <= y < height) and
                    not marks[y][x]
                )
            ]
        )

        if any(possible):
            return True
        else:
            marks[current_cell.y][current_cell.x] = False
            return False

    def exist(
        self,
        board: List[List[str]],
        word: str,
    ) -> bool:

        width = len(board[0])
        height = len(board)
        marks = [
            [
                False
                for _ in range(width)
            ]
            for _ in range(height)
        ]

        return any(
            self.attempt(
                board=board,
                marks=marks,
                width=width,
                height=height,
                word=word,
                depth=0,
                current_cell=Cell(
                    x=x,
                    y=y,
                    character=board[y][x],
                )
            )
            for x, y in product(
                range(0, width),
                range(0, height),
            )
        )


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.exist(
            board=[
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            word="ABCCED",
        )
    )
    print(
        solution.exist(
            board=[
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            word="SEE",
        )
    )
    print(
        solution.exist(
            board=[
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            word="ABCB",
        )
    )
