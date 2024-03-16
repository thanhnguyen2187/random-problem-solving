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
    reduce,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]
        for num in nums:
            prefixes.append(prefixes[-1] * num)
        prefixes.append(1)

        postfixes = [1]
        for num in reversed(nums):
            postfixes.append(postfixes[-1] * num)
        postfixes.append(1)
        postfixes.reverse()

        result = [
            prefixes[i - 1] * postfixes[i + 1]
            for i in range(1, len(nums) + 1)
        ]
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.productExceptSelf(nums=[1, 2, 3, 4]))
