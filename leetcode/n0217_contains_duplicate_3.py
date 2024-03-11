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
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter()
        for num in nums:
            counter[num] += 1
            if counter[num] >= 2:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()
