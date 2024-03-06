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
    def reverseBits(self, n: int) -> int:
        reversed_str = ''.join(reversed(bin(n)[2:]))
        while len(reversed_str) < 32:
            reversed_str += '0'
        return int('0b' + reversed_str, 2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseBits(n=43261596))
