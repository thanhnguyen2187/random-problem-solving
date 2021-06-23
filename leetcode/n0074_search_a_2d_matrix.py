from typing import (
    List,
)
from itertools import (
    zip_longest,
)
from bisect import (
    bisect,
    bisect_left,
)


class Solution:

    def searchMatrix(
        self,
        matrix: List[List[int]],
        target: int,
    ) -> bool:

        row_index = bisect_left(
            a=[
                matrix[index][0]
                for index in range(len(matrix))
            ],
            x=target,
        )
        if row_index > len(matrix):
            return False
        elif row_index == len(matrix):
            row_index -= 1

        column_index = bisect_left(
            a=matrix[row_index],
            x=target
        )
        if column_index >= len(matrix[0]):
            return False

        if matrix[row_index][column_index] == target:
            return True

        if (
            column_index == 0 and
            row_index > 0
        ):
            row_index -= 1
            column_index = bisect_left(
                a=matrix[row_index],
                x=target
            )
            if column_index >= len(matrix[0]):
                return False

        return matrix[row_index][column_index] == target


if __name__ == '__main__':
    solution = Solution()

    # matrix = [
    #     [1],
    # ]
    # print(
    #     solution.searchMatrix(
    #         matrix=matrix,
    #         target=2,
    #     )
    # )

    # matrix = [
    #     [1, 3],
    # ]
    # print(
    #     solution.searchMatrix(
    #         matrix=matrix,
    #         target=3,
    #     )
    # )

    matrix = [
        [1],
        [3],
    ]
    print(
        solution.searchMatrix(
            matrix=matrix,
            target=2,
        )
    )

    # matrix = [
    #     [1, 3, 5, 7],
    #     [10, 11, 16, 20],
    #     [23, 30, 34, 60],
    # ]
    # print(
    #     solution.searchMatrix(
    #         matrix=matrix,
    #         target=13,
    #     )
    # )


    # matrix = [
    #     [1, 3, 5, 7],
    #     [10, 11, 16, 20],
    #     [23, 30, 34, 60],
    # ]
    # print(
    #     solution.searchMatrix(
    #         matrix=matrix,
    #         target=3,
    #     )
    # )
