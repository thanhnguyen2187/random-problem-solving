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
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(
            char.lower()
            for char in s
            if char.isalnum()
        )
        n = len(s)
        for i in range(n // 2):
            j = n - i - 1
            if s[i] != s[j]:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
