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
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        results = [
            [0 for _ in range(n + 1)]
            for _ in range(m + 1)
        ]
        for j in range(1, n + 1):
            results[0][j] = j
        for i in range(1, m + 1):
            results[i][0] = i

        for i, j in product(range(1, m + 1), range(1, n + 1)):
            if word1[i - 1] == word2[j - 1]:
                results[i][j] = results[i - 1][j - 1]
            else:
                results[i][j] = 1 + min(
                    results[i - 1][j],
                    results[i][j - 1],
                    results[i - 1][j - 1],
                )

        return results[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance(word1="horse", word2="ros"))
    print(solution.minDistance(word1="sea", word2="eat"))
    print(solution.minDistance(word1="intention", word2="execution"))
