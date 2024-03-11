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
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case _ if (
                    # positive number
                    token.isdecimal()
                    # negative number
                    or token.startswith('-') and token[1:].isdecimal()
                ):
                    stack.append(int(token))
                case '+':
                    result = stack.pop()
                    result += stack.pop()
                    stack.append(result)
                case '-':
                    a = stack.pop()
                    b = stack.pop()
                    result = b - a
                    stack.append(result)
                case '/':
                    a = stack.pop()
                    b = stack.pop()
                    result = math.trunc(b / a)
                    stack.append(result)
                case '*':
                    result = stack.pop()
                    result *= stack.pop()
                    stack.append(result)
                case _:
                    raise Exception('unreachable code')

        return int(stack[0])


if __name__ == '__main__':
    solution = Solution()
    # print(solution.evalRPN(tokens=["2", "1", "+", "3", "*"]))
    # print(solution.evalRPN(tokens=["4", "13", "5", "/", "+"]))
    print(solution.evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
