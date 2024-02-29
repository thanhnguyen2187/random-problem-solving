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


def is_palindrome(s: str) -> bool:
    n = len(s)
    for i in range(0, n // 2):
        if s[i] != s[n - i - 1]:
            return False

    return True


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def recurse(i: int, current: tuple, total: int):
            if total >= len(s):
                result.append(current)
                return

            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if is_palindrome(word):
                    recurse(i=j, current=(*current, word), total=total + len(word))

        recurse(i=0, current=(), total=0)
        return result


if __name__ == '__main__':
    solution = Solution()
    # print(is_palindrome(s="aa"))
    print(solution.partition(s="aab"))
