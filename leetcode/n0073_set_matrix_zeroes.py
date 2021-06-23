from typing import (
    List,
)
from itertools import (
    zip_longest,
)


class Solution:

    def setZeroes(
        self,
        matrix: List[List[int]],
    ) -> None:
        row_count = len(matrix)
        column_count = len(matrix[0])
        row_index_zeroes = set()
        column_index_zeroes = set()

        for row_index in range(row_count):
            for column_index in range(column_count):
                if matrix[row_index][column_index] == 0:
                    row_index_zeroes.add(row_index)
                    column_index_zeroes.add(column_index)

        for row_index in range(row_count):
            for column_index in range(column_count):
                if (
                    row_index in row_index_zeroes or
                    column_index in column_index_zeroes
                ):
                    matrix[row_index][column_index] = 0


if __name__ == '__main__':
    solution = Solution()

    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
    solution.setZeroes(matrix=matrix)
    print(matrix)

    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5],
    ]
    solution.setZeroes(matrix=matrix)
    print(matrix)
