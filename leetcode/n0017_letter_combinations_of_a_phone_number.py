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


digit_to_chars = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        chars_options = [
            digit_to_chars[digit]
            for digit in digits
        ]
        options = [
            option
            for option in product(*chars_options)
        ]
        result = [
            ''.join(option)
            for option in options
        ]
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations(digits="23"))
    print(solution.letterCombinations(digits=""))
