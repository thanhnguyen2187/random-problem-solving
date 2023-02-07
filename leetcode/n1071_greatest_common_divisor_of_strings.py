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


def str_mod(str_1: str, str_2: str) -> str:
    while str_1.startswith(str_2):
        str_1 = str_1[len(str_2):]
    return str_1


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str2 == "":
            return str1
        elif len(str2) > len(str1):
            return self.gcdOfStrings(
                str1=str2,
                str2=str1,
            )
        else:
            new_str_2 = str_mod(str_1=str1, str_2=str2)
            if new_str_2 == str1:
                return ""
            return self.gcdOfStrings(
                str1=str2,
                str2=new_str_2,
            )


if __name__ == '__main__':
    solution = Solution()
    # print(solution.gcdOfStrings(str1="ABCABC", str2="ABC"))
    # print(solution.gcdOfStrings(str1="ABABAB", str2="ABAB"))
    # print(solution.gcdOfStrings(str1="LEET", str2="CODE"))
    print(solution.gcdOfStrings(str1="TAUXXTAUXXTAUXXTAUXXTAUXX", str2="TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
