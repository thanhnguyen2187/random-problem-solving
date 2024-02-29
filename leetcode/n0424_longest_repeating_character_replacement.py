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
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter([s[0]])

        max_count = 1
        max_char = 1
        l = 0
        r = 1
        while r < len(s):
            counter[s[r]] += 1
            if counter[s[r]] > max_char:
                max_char = counter[s[r]]
            while (r - l + 1) - max_char > k:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1
            max_count = max(
                max_count,
                r - l + 1,
            )

            r += 1

        return max_count


if __name__ == '__main__':
    solution = Solution()
    print(solution.characterReplacement(s="ABABBA", k=2))
