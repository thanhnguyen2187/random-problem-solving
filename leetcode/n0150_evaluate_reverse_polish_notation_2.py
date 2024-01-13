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


def add(first, second):
    return first + second


def minus(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    return math.trunc(first / second)


def create_evaluator():
    stack = []
    operator_dict = {
        "+": add,
        "-": minus,
        "*": multiply,
        "/": divide,
    }

    def evaluate(expr: str):
        nonlocal stack
        match expr:
            case "+" | "-" | "*" | "/":
                first = int(stack.pop())
                second = int(stack.pop())
                operator_func = operator_dict[expr]
                value = operator_func(second, first)
                stack.append(value)
            case _:
                stack.append(expr)

    def get_value():
        return int(stack[0])

    return evaluate, get_value


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evaluate, get_value = create_evaluator()
        for token in tokens:
            evaluate(token)

        return get_value()


if __name__ == '__main__':
    solution = Solution()
    # print(solution.evalRPN(tokens=["2", "1", "+", "3", "*"]))
    # print(solution.evalRPN(tokens=["4", "13", "5", "/", "+"]))
    print(solution.evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
