from typing import (
    List,
    NamedTuple,
)
from itertools import (
    accumulate,
)
from bisect import (
    bisect_left,
    bisect_right,
    insort,
    insort_left,
)


class Solution:

    def find_subarray_sum(
        self,
        sums_prefixed: List[int],
        k: int,
    ) -> int:

        sums_encountered = [
            0,
            float("inf"),
        ]
        sum_max = float("-inf")

        for sum_right in sums_prefixed:
            target = sum_right - k
            sum_left_index = bisect_left(
                a=sums_encountered,
                x=target,
            )
            sum_left = sums_encountered[sum_left_index]

            sum_current = sum_right - sum_left
            sum_max = max(
                sum_max,
                sum_current,
            )

            insort(
                a=sums_encountered,
                x=sum_right,
            )

        return sum_max

    def maxSumSubmatrix(
        self,
        matrix: List[List[int]],
        k: int,
    ) -> int:
        # step 1: turn the rows into prefix sums
        matrix = [
            list(accumulate(row))
            for row in matrix
        ]
        row_length = len(matrix)

        # step 2: use a nested for loop
        sum_max = float("-inf")
        for row_first_index in range(row_length):
            row_first = matrix[row_first_index]
            for row_second_index in range(row_first_index, row_length):
                if row_second_index != row_first_index:
                    row_second = matrix[row_second_index]
                    row_first = list(
                        map(
                            lambda first, second: first + second,
                            row_first,
                            row_second,
                        )
                    )
                sum_max = max(
                    sum_max,
                    self.find_subarray_sum(
                        sums_prefixed=row_first,
                        k=k,
                    )
                )

        return sum_max


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.maxSumSubmatrix(
            matrix=[
                [1, 0, 1],
                [0, -2, 3],
            ],
            k=2,
        )
    )
    print(
        solution.maxSumSubmatrix(
            matrix=[
                [2, 2, -1],
            ],
            k=3,
        )
    )
    print(
        solution.maxSumSubmatrix(
            matrix=[
                [10, 28, -20],
                [11, -9, 3],
                [2, 4, 0],
            ],
            k=14,
        )
    )
