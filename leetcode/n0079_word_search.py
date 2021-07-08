from typing import (
    List,
    NamedTuple,
)


class Coordinate(NamedTuple):
    x: int
    y: int


class Solution:

    def attempt(
        self,
        board: List[List[str]],
        marks: List[List[bool]],
        width: int,
        height: int,
        word: str,
        current_word: str,
        current_coordinate: Coordinate,
    ) -> bool:

        current_word += board[current_coordinate.y][current_coordinate.x]
        if not word.startswith(current_word):
            return False
        elif word == current_word:
            return True

        marks[current_coordinate.y][current_coordinate.x] = True

        possible = [
            self.attempt(
                board=board,
                marks=marks,
                width=width,
                height=height,
                word=word,
                current_word=current_word,
                current_coordinate=coordinate,
            )
            for coordinate in [
                Coordinate(x=current_coordinate.x - 1, y=current_coordinate.y),
                Coordinate(x=current_coordinate.x + 1, y=current_coordinate.y),
                Coordinate(x=current_coordinate.x, y=current_coordinate.y - 1),
                Coordinate(x=current_coordinate.x, y=current_coordinate.y + 1),
            ]
            if (
                (0 <= coordinate.x < width) and
                (0 <= coordinate.y < height) and
                not marks[coordinate.y][coordinate.x]
            )
        ]

        # if x != current_coordinate.x and y != current_coordinate.y
        marks[current_coordinate.y][current_coordinate.x] = False

        return any(possible)


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
                current_word="",
                current_coordinate=Coordinate(x=x, y=y),
            )
            for x in range(width)
            for y in range(height)
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
