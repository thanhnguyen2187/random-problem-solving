from typing import List


class MinStack:
    def __init__(self):
        self.stack = []
        self.stack_min = [2 ** 31 - 1]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stack_min.append(
            min(val, self.stack_min[-1])
        )

    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]


if __name__ == "__main__":
    min_stack = MinStack()
    # min_stack.push(1)
    # min_stack.push(2)
    # min_stack.push(0)
    # print(min_stack.getMin())
    # min_stack.pop()
    # print(min_stack.top())
    # print(min_stack.getMin())
    min_stack.push(-1)
    min_stack.push(3)
    min_stack.push(-4)
    print(min_stack.getMin())
    min_stack.pop()
    print(min_stack.getMin())
    print(min_stack.top())
