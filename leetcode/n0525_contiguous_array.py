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
    cache,
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        acc = [0]
        for num in nums:
            if num == 0:
                acc.append(acc[-1] - 1)
            elif num == 1:
                acc.append(acc[-1] + 1)

        encountered = {}
        result = 0
        for i, a in enumerate(acc):
            if a in encountered:
                result = max(result, i - encountered[a])
            else:
                encountered[a] = i

        return result


if __name__ == '__main__':
    solution = Solution()
    # print(solution.findMaxLength(nums=[0, 1]))
    print(solution.findMaxLength(nums=[0, 1, 0, 1]))
    print(solution.findMaxLength(nums=[0, 0, 0, 1]))
    print(solution.findMaxLength(nums=[0, 0, 0, 1, 0, 1]))
    # print(solution.findMaxLength(nums=[0, 1, 1, 0, 1, 1, 1, 0]))
