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
    def partitionString(self, s: str) -> int:
        result = 1
        cache = set()
        for char in s:
            if char in cache:
                result += 1
                cache = set()
            cache.add(char)

        return result


if __name__ == '__main__':
    solution = Solution()
    # print(solution.partitionString("abacaba"))
    # print(solution.partitionString("ssssss"))
    # print(solution.partitionString("abracadabra"))
    print(solution.partitionString("abccacc"))
    print(solution.partitionString("a"))
