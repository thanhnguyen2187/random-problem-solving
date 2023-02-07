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
        def frozendict(dict_) -> tuple:
            return tuple(
                (k, v)
                for k, v in sorted(dict_.items())
            )

        s2_substrings = [
            s2[index:index + len(s1)]
            for index in range(len(s2) - len(s1) + 1)
        ]
        s2_substring_counters = {
            frozendict(Counter(substring))
            for substring in s2_substrings
        }
        return frozendict(Counter(s1)) in s2_substring_counters


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkInclusion(s1="ab", s2="eidbaooo"))
    print(solution.checkInclusion(s1="ab", s2="eidaooo"))
    print(solution.checkInclusion(s1="adc", s2="dcda"))
