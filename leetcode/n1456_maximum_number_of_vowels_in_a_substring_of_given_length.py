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


def extract_result(char_counter: Counter):
    return sum((
        char_counter['a'],
        char_counter['e'],
        char_counter['i'],
        char_counter['o'],
        char_counter['u'],
    ))


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window = (0, k)
        char_counter = Counter(s[window[0]:window[1]])
        result = extract_result(char_counter=char_counter)

        while window[1] < len(s):
            window_start, window_end = window
            char_start, char_end = s[window_start], s[window_end]
            char_counter[char_start] -= 1
            char_counter[char_end] += 1

            result = max(result, extract_result(char_counter=char_counter))
            window = (window_start + 1, window_end + 1)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxVowels(s="abciiidef", k=3))
    print(solution.maxVowels(s="aeiou", k=2))
    print(solution.maxVowels(s="aeiou", k=5))
