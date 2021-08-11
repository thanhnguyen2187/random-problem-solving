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
    row_index: int
    column_index: int


class Solution:

    def calculate(
        self,
        row_count,
        column_count,
        row_ranks: List[List[int]],
        column_ranks: List[List[int]],
        best_ranks: List[List[int]],
        row_index: int,
        column_index: int,
    ) -> int:

        """
        Calculate the best rank by checking if the equivalent position in column ranks or row ranks have any lower rank.
        If there are lower ranks, return the maximum best rank of these lower ranks, plus one.

        :param row_count:
        :param column_count:
        :param row_ranks:
        :param column_ranks:
        :param best_ranks:
        :param row_index:
        :param column_index:
        :return:
        """

        # base case: the rank is the lowest
        if best_ranks[row_index][column_index] == 1:
            return 1

        # the rank was not calculated
        elif best_ranks[row_index][column_index] == 0:
            row_rank = row_ranks[row_index][column_index]
            # lower column index within the same row
            row_lower_positions = [
                (row_index, column_index)
                for column_index in range(column_count)
                if row_ranks[row_index][column_index] == row_rank - 1
            ]
            # row_equal_positions = [
            #     (row_index, index)
            #     for index in range(column_count)
            #     if (
            #         row_ranks[row_index][index] == row_rank and
            #         index != column_index
            #     )
            # ]

            column_rank = column_ranks[row_index][column_index]
            # lower row index within the same column
            column_lower_positions = [
                (row_index, column_index)
                for row_index in range(row_count)
                if column_ranks[row_index][column_index] == column_rank - 1
            ]
            # column_equal_positions = [
            #     (index, column_index)
            #     for index in range(row_count)
            #     if (
            #         column_ranks[index][column_index] == column_rank and
            #         index != row_index
            #     )
            # ]

            lower_positions = [
                *row_lower_positions,
                *column_lower_positions,
            ]
            # equal_positions = [
            #     *row_equal_positions,
            #     *column_equal_positions,
            # ]

            best_rank = 1
            best_rank_lower_positions = 0
            # best_rank_equal_positions = 0
            if len(lower_positions) != 0:
                best_rank_lower_positions = 1 + max(
                    self.calculate(
                        row_count=row_count,
                        column_count=column_count,
                        row_ranks=row_ranks,
                        column_ranks=column_ranks,
                        best_ranks=best_ranks,
                        row_index=row_index,
                        column_index=column_index,
                    )
                    for (row_index, column_index) in lower_positions
                )
            # if len(equal_positions) != 0:
            #     best_rank_equal_positions = max(
            #         self.calculate(
            #             row_count=row_count,
            #             column_count=column_count,
            #             row_ranks=row_ranks,
            #             column_ranks=column_ranks,
            #             best_ranks=best_ranks,
            #             row_index=row_index,
            #             column_index=column_index,
            #         )
            #         for (row_index, column_index) in equal_positions
            #     )

            best_rank = max(
                best_rank,
                # best_rank_equal_positions,
                best_rank_lower_positions,
            )
            best_ranks[row_index][column_index] = best_rank
            return best_rank

        # the rank was calculated
        else:
            return best_ranks[row_index][column_index]


    def matrixRankTransform(
        self,
        matrix: List[List[int]],
    ) -> List[List[int]]:

        row_count = len(matrix)
        column_count = len(matrix[0])

        def create_ranks() -> List[List[int]]:
            return [
                [
                    0
                    for _ in range(column_count)
                ]
                for _ in range(row_count)
            ]
        row_ranks = create_ranks()
        column_ranks = create_ranks()
        best_ranks = create_ranks()

        for row_index, row in enumerate(matrix):
            row_sorted = sorted(set(row))
            for column_index, value in enumerate(row):
                rank = bisect_left(
                    a=row_sorted,
                    x=value,
                )
                row_ranks[row_index][column_index] = rank + 1

        for column_index in range(column_count):
            column = list(
                map(
                    lambda row: row[column_index],
                    matrix,
                )
            )
            column_sorted = sorted(set(column))
            for row_index, value in enumerate(column):
                rank = bisect_left(
                    a=column_sorted,
                    x=value,
                )
                column_ranks[row_index][column_index] = rank + 1


        for row_index, column_index in product(
            range(row_count),
            range(column_count),
        ):
            self.calculate(
                row_count=row_count,
                column_count=column_count,
                row_ranks=row_ranks,
                column_ranks=column_ranks,
                best_ranks=best_ranks,
                row_index=row_index,
                column_index=column_index,
            )

        return best_ranks


if __name__ == '__main__':
    solution = Solution()

    for matrix in [
        [
            [-37, -50, -3, 44],
            [-37, 46, 13, -32],
            [47, -42, -3, -40],
            [-17, -22, -39, 24],
        ],
        [
            [1, 2],
            [3, 4],
        ],
        [
            [20, -21, 14],
            [-19, 4, 19],
            [22, -47, 24],
            [-19, 4, 19],
        ],
        [
            [7, 3, 6],
            [1, 4, 5],
            [9, 8, 2],
        ],
    ]:
        print(
            solution.matrixRankTransform(matrix=matrix)
        )
