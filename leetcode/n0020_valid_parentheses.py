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
    def isValid(self, s: str) -> bool:
        open_to_close = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        close_to_open = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for char in s:
            if char in open_to_close:
                stack.append(char)
            elif char in close_to_open and stack:
                last_char = stack[-1]
                if last_char == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()
