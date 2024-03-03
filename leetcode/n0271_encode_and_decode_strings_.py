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

    def encode(self, strs: List[str]) -> str:
        strs.append(str(len(strs)))
        return '\0'.join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split('\0')[:-1]



if __name__ == '__main__':
    solution = Solution()
