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
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        push_index = 0
        pop_index = 0
        n = len(pushed)
        while push_index < n:
            if pushed[push_index]:
                ...


if __name__ == '__main__':
    solution = Solution()
