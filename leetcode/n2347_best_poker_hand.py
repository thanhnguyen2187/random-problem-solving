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
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        ranks_counter = Counter(ranks)
        highest_rank_count = max(ranks_counter.values())
        if highest_rank_count >= 3:
            return "Three of a Kind"
        elif highest_rank_count == 2:
            return "Pair"
        else:
            return "High Card"


if __name__ == '__main__':
    solution = Solution()
