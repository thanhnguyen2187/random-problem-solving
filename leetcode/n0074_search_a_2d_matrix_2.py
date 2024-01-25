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
import bisect
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


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_column = [
            row[0]
            for row in matrix
        ]
        found_row_index = bisect.bisect_left(first_column, target)
        if found_row_index < len(first_column) and first_column[found_row_index] == target:
            return True

        found_row_index = max(0, found_row_index - 1)

        found_row = matrix[found_row_index]
        found_column_index = bisect.bisect_left(found_row, target)
        found_target = (
            found_column_index < len(found_row) and
            found_row[found_column_index] == target
        )
        return found_target



if __name__ == '__main__':
    solution = Solution()
    # print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
    # print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=1))
    # print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=16))
    # print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=59))
    # print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=0))
    print(solution.searchMatrix(matrix=[[1], [3]], target=3))
