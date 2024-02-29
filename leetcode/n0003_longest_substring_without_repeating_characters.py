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
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        i, j = 0, 1
        chars = {s[i]}
        max_length = 1

        while j < n:
            if s[j] in chars:
                max_length = max(max_length, len(chars))
                while s[j] in chars:
                    chars.remove(s[i])
                    i += 1

            chars.add(s[j])
            j += 1

        max_length = max(max_length, len(chars))

        return max_length


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s="aab"))
    print(solution.lengthOfLongestSubstring(s="dvdf"))
    print(solution.lengthOfLongestSubstring(s="abcdabaacdefga"))
