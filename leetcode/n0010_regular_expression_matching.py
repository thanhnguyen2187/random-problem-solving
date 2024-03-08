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
    def isMatch(self, s: str, p: str) -> bool:
        p_units = []
        for char in p:
            if char == '*':
                # We can do this since the description stated that:
                #
                # > It is guaranteed for each appearance of the character '*',
                #   there will be a previous valid character to match.
                p_units[-1] = p_units[-1] + '*'
                continue
            p_units.append(char)

        m = len(p_units)
        n = len(s)
        # We create the result table for each unit of pattern and each
        # character. The first items are accounted for empty string and empty
        # pattern.
        results = [
            [False for _ in range(n + 1)]
            for _ in range(m + 1)
        ]
        results[0][0] = True
        # Handle special cases where the star can be substituted for empty
        # string, therefore matches the empty string.
        for i in range(1, m + 1):
            if p_units[i - 1].endswith('*'):
                results[i][0] = results[i - 1][0]

        for i, j in product(range(1, m + 1), range(1, n + 1)):
            if p_units[i - 1][0] == s[j - 1] or p_units[i - 1][0] == '.':
                results[i][j] = results[i - 1][j - 1]
                if p_units[i - 1].endswith('*'):
                    results[i][j] = results[i][j - 1]
            if p_units[i - 1].endswith('*'):
                results[i][j] = (
                    results[i][j] or
                    # In case the pattern unit accounts to nothing
                    results[i - 1][j]
                )

        return results[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    # print(solution.isMatch(s="abc", p="a*b*c*"))
    # print(solution.isMatch(s="aa", p="a*"))
    # print(solution.isMatch(s="ab", p=".*"))
    # print(solution.isMatch(s="aaabbbccc", p="a*b*c*d*"))
    # print(solution.isMatch(s="aabbcc", p="c*a*b*"))
    print(solution.isMatch(s="aaa", p="ab*a*c*a"))
