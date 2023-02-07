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


def is_palindrome(text: str):
    return text == text[::-1]


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        if n == 1:
            return [[s]]

        position_groups = []
        for position_length in range(1, n):
            position_groups.extend(
                list(combinations(range(1, n), position_length))
            )

        results = []
        for positions in position_groups:
            substrings = [
                s[begin:end]
                for begin, end in zip(
                    (0, *positions),
                    (*positions, len(s)),
                )
            ]
            if all(map(is_palindrome, substrings)):
                results.append(substrings)

        if is_palindrome(s):
            results.append([s])
        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.partition(s="aab"))
    print(solution.partition(s="abcaa"))
    print(solution.partition(s="a"))
    print(solution.partition(s="bb"))
