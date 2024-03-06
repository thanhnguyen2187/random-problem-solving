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
    def partitionLabels(self, s: str) -> List[int]:
        last_indexes = {
            s[i]: i
            for i in range(len(s))
        }

        tracked = set()
        results = [0]
        i = 0
        last = 0
        while i <= len(s) - 1:
            results[-1] += 1
            last = max(last, last_indexes[s[i]])
            if i == last:
                results.append(0)
            tracked.add(s[i])
            i += 1

        # remove redundant 0 that is always append at the end
        results.pop()

        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.partitionLabels(s="abcabdedddga"))
    print(solution.partitionLabels(s="abc"))
    print(solution.partitionLabels(s="ababcbacadefegdehijhklij"))
