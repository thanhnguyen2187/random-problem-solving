import math
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
)


class ListNode:
    def __init__(
        self,
        x: int,
        next: Optional['ListNode'] = None,
    ):
        self.val: int = x
        self.next: 'ListNode' = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: 'TreeNode' = None,
        right: 'TreeNode' = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # noinspection PyPep8Naming
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[-1])

        operators = {'+', '-', '*', '/'}
        stack = []
        for token in tokens:
            if token in operators:
                current_result = eval(f'math.trunc({stack[-2]} {token} {stack[-1]})')
                stack = stack[:-2]
                stack.append(current_result)
            else:
                stack.append(token)

        return stack[-1]


if __name__ == '__main__':
    solution = Solution()
    # solution.evalRPN(tokens=["0"])
    # print(solution.evalRPN(tokens=["2", "1", "+", "3", "*"]))
    # print(solution.evalRPN(tokens=["4", "13", "5", "/", "+"]))
    print(solution.evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
