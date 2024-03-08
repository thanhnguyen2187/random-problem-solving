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
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, o = len(s1), len(s2), len(s3)
        if m + n != o:
            return False

        @cache
        def recurse(i: int, j: int, k: int):
            if i == -1:
                return s2[:j + 1] == s3[:k + 1]
            elif j == -1:
                return s1[:i + 1] == s3[:k + 1]

            if s1[i] == s3[k] and s2[j] == s3[k]:
                return recurse(i - 1, j, k - 1) or recurse(i, j - 1, k - 1)
            elif s1[i] == s3[k]:
                return recurse(i - 1, j, k - 1)
            elif s2[j] == s3[k]:
                return recurse(i, j - 1, k - 1)
            else:
                return False

        return recurse(i=m - 1, j=n - 1, k=o - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
    print(solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
    print(solution.isInterleave(s1="", s2="", s3=""))
    print(solution.isInterleave(s1="aabc", s2="abad", s3="aabadabc"))
