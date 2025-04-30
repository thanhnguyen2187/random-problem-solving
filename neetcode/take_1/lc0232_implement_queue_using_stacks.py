from typing import List


class MyQueue:

    def __init__(self):
        self.index = 0
        self.stack_1 = []

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        top = self.stack_1[self.index]
        self.index += 1
        return top

    def peek(self) -> int:
        return self.stack_1[self.index]

    def empty(self) -> bool:
        return self.index == len(self.stack_1)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


if __name__ == "__main__":
    obj = MyQueue()
    # obj.push(1)
    # obj.push(1)
    # print(obj.pop())
    # print(obj.empty())

    obj.push(1)
    obj.push(2)
    print(obj.pop())
    obj.push(3)
    print(obj.pop())
    print(obj.pop())
    obj.push(4)
    print(obj.pop())
    print(obj.empty())
