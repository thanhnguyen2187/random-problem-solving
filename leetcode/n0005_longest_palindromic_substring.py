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


def is_palindrome(s: str):
    n = len(s)
    for i in range(0, n // 2):
        if s[i] != s[n - i - 1]:
            return False

    return True


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ''
        for i in range(n):
            l, r = i, i
            while (
                0 <= l < n and
                0 <= r < n and
                s[l] == s[r]
            ):
                longest = max(longest, s[l:r + 1], key=len)
                l -= 1
                r += 1

            l, r = i, i + 1
            while (
                0 <= l < n and
                0 <= r < n and
                s[l] == s[r]
            ):
                longest = max(longest, s[l:r + 1], key=len)
                l -= 1
                r += 1

        return longest


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome(s="babad"))
