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
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        spell_scores = [
            success / spell
            for spell in spells
        ]
        potions = sorted(potions)
        n = len(potions)
        success_counts = [
            n - bisect_left(potions, spell_score)
            for spell_score in spell_scores
        ]
        return success_counts


if __name__ == '__main__':
    solution = Solution()
