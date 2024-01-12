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


def is_palindrome(s: str) -> bool:
    return "".join(reversed(s)) == s


class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = "".join(
            character.lower()
            for character in s
            if character.lower() in frozenset("abcdefghijklmnopqrstuvwxyz1234567890")
        )

        return is_palindrome(s=filtered_s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(s="A man, a plan, a canal: Panama"))
    print(solution.isPalindrome(s="race a car"))
    print(solution.isPalindrome(s=" "))
