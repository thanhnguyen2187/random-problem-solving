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


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = len(numbers) - 1

        while left_index <= right_index:
            total = numbers[left_index] + numbers[right_index]
            if total == target:
                return [left_index + 1, right_index + 1]
            elif total > target:
                right_index -= 1
            elif total < target:
                left_index += 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum(numbers=[2, 7, 11, 15], target=9))
    print(solution.twoSum(numbers=[2, 3, 4], target=6))
    print(solution.twoSum(numbers=[-1, 0], target=-1))
