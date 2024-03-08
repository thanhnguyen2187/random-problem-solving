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
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        results = [
            [0 for _ in range(n + 1)]
            for _ in range(m + 1)
        ]

        for i, j in product(range(1, m + 1), range(1, n + 1)):
            results[i][j] = max(
                results[i - 1][j],
                results[i][j - 1],
            )
            if text1[i - 1] == text2[j - 1]:
                results[i][j] = results[i - 1][j - 1] + 1

        return results[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonSubsequence(text1="abcde", text2="ace"))
    print(solution.longestCommonSubsequence(text1="abc", text2="def"))
