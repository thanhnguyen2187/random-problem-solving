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
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda pair: (pair[0], -pair[1]))

        n = len(envelopes)
        results = list(repeat(1, n))

        for i in reversed(range(0, n - 1)):
            for j in range(i + 1, n):
                e1 = envelopes[i]
                e2 = envelopes[j]
                if e1[0] < e2[0] and e1[1] < e2[1]:
                    results[i] = max(results[i], results[j] + 1)

        return results[0]


if __name__ == '__main__':
    solution = Solution()
    # print(solution.maxEnvelopes(envelopes=[[5, 4], [6, 4], [6, 7], [2, 3]]))
    # print(solution.maxEnvelopes(envelopes=[[1, 3], [3, 5], [6, 7], [6, 8], [8, 4], [9, 5]]))
    # print(solution.maxEnvelopes(envelopes=[[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]))
    print(solution.maxEnvelopes(envelopes=[[46, 89], [50, 53], [52, 68], [72, 45], [77, 81]]))
