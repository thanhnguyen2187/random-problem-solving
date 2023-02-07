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
)


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        columns = [
            ''.join(characters)
            for characters in zip(*strs)
        ]
        strs_valid = [
            list(column) == sorted(column)
            for column in columns
        ]
        count = sum(
            1 if not validity else 0
            for validity in strs_valid
        )
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDeletionSize(strs=["cba", "daf", "ghi"]))
    print(solution.minDeletionSize(strs=["zyx", "wvu", "tsr"]))
