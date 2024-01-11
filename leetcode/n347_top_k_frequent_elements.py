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
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_kv_pairs = sorted(
            counter.items(),
            key=lambda kv_pair: kv_pair[1],
            reverse=True,
        )
        result = [
            kv_pair[0]
            for kv_pair in sorted_kv_pairs[:k]
        ]
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent(nums=[1,1,1,2,2,3], k=2))
