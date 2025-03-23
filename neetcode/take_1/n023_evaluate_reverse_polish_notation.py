import math
from typing import List


def is_operator(token: str):
    return str in ["+", "-", "/", "*"]


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+":
                    operand_1 = stack.pop()
                    operand_2 = stack.pop()
                    stack.append(operand_2 + operand_1)
                case "-":
                    operand_1 = stack.pop()
                    operand_2 = stack.pop()
                    stack.append(operand_2 - operand_1)
                case "*":
                    operand_1 = stack.pop()
                    operand_2 = stack.pop()
                    stack.append(operand_2 * operand_1)
                case "/":
                    operand_1 = stack.pop()
                    operand_2 = stack.pop()
                    stack.append(int(float(operand_2) / operand_1))
                case _:
                    stack.append(int(token))

        return stack[0]


if __name__ == "__main__":
    solution = Solution()
    # tokens = ["1", "2", "+", "3", "*", "4", "-"]
    # => 5
    # tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    # => 22
    # tokens = ["4", "13", "5", "/", "+"]
    # => 6
    result = solution.evalRPN(tokens=tokens)
    print(result)
