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
    cache,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


@cache
def is_scramble(s1: str, s2: str) -> bool:
    if Counter(s1) != Counter(s2):
        return False
    if len(s1) <= 3:
        return True

    s1_pairs = [
        (s1[:i], s1[i:])
        for i in range(1, len(s1))
    ]
    for s1_1, s1_2 in s1_pairs:
        s2_1 = s2[:len(s1_1)]
        s2_2 = s2[len(s1_1):]
        s2_3 = s2[:len(s1_2)]
        s2_4 = s2[len(s1_2):]
        if (
            is_scramble(s1=s1_1, s2=s2_1) and
            is_scramble(s1=s1_2, s2=s2_2)
        ) or (
            is_scramble(s1=s1_1, s2=s2_4) and
            is_scramble(s1=s1_2, s2=s2_3)
        ):
            return True

    return False


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return is_scramble(s1=s1, s2=s2)


if __name__ == '__main__':
    solution = Solution()

    print(solution.isScramble(s1="abcd", s2="badc"))
    print(solution.isScramble(s1="abcd", s2="cabd"))
    print(solution.isScramble(s1="abcd", s2="cadb"))
    print(solution.isScramble(s1="aaccd", s2="acaad"))
    print(solution.isScramble(s1="oatzzffqpnwcxhejzjsnpmkmzngneo", s2="acegneonzmkmpnsjzjhxwnpqffzzto"))
    print(solution.isScramble(s1="eebaacbcbcadaaedceaaacadccd", s2="eadcaacabaddaceacbceaabeccd"))
    # print(strip_common_left(s1="abc", s2="abc"))
    # print(strip_common_left(s1="abcde", s2="abced"))
    # print(strip_common_right(s1="feabc", s2="rdabc"))
    # print(strip_common_right(s1="abc", s2="abc"))
