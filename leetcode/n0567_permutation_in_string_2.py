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
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        set_1 = Counter(s1)
        l = 0
        r = len(s1)
        set_2 = Counter(s2[l:r])
        if set_1 == set_2:
            return True

        while r < len(s2):
            set_2[s2[l]] -= 1
            set_2[s2[r]] += 1
            if set_1 == set_2:
                return True
            l += 1
            r += 1

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkInclusion(s1="aba", s2="cdeabaaf"))
