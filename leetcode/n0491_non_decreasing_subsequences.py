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


def is_non_decreasing(numbers: List[int]) -> bool:
    return all(
        number_1 <= number_2
        for number_1, number_2 in zip(numbers, numbers[1:])
    )


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = set()
        for count in range(2, n + 1):
            valid_results = [
                elements
                for elements in combinations(nums, count)
                if is_non_decreasing(elements)
            ]
            results.update(valid_results)
        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.findSubsequences(nums=[4, 6, 7, 7]))
