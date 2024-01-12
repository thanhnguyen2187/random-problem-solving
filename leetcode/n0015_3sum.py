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


def two_sum(nums: List[int], target: int) -> List[int]:
    if len(nums) < 2:
        return []

    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        total = nums[left_index] + nums[right_index]
        if total == target:
            return [left_index, right_index]
        elif total < target:
            left_index += 1
        elif total > target:
            right_index += 1

    return []


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = set()

        for i in range(0, len(nums) - 1):
            left_index = i + 1
            right_index = len(nums) - 1
            current = nums[i]

            while left_index < right_index:
                left = nums[left_index]
                right = nums[right_index]
                total = left + right + current
                if total == 0:
                    results.add((current, left, right))
                    left_index += 1
                elif total < 0:
                    left_index += 1
                elif total > 0:
                    right_index -= 1

        return results


if __name__ == '__main__':
    solution = Solution()
    # print(solution.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
    print(solution.threeSum(nums=[1,2,-2,-1]))
