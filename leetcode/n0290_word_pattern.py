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
    Counter,
)


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        pairs = set(zip(words, pattern))
        first_element_counter = Counter(pair[0] for pair in pairs)
        second_element_counter = Counter(pair[1] for pair in pairs)
        return all(
            value == 1
            for value in first_element_counter.values()
        ) and all(
            value == 1
            for value in second_element_counter.values()
        )


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordPattern(pattern="abba", s="dog cat cat dog"))
    print(solution.wordPattern(pattern="abba", s="dog cat cat fish"))
    print(solution.wordPattern(pattern="aba", s="dog cat cat"))
