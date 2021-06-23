from typing import (
    List,
    NamedTuple,
    Literal,
    Set,
)
from collections import (
    namedtuple,
)
from itertools import (
    product,
)


class Element(NamedTuple):
    value: int
    type: Literal["open", "close"]


class Solution:

    def merge(
        self,
        intervals: List[List[int]],
    ) -> List[List[int]]:

        groups: List[List[int]] = []
        elements: List[Element] = []
        stack: List[Element] = []
        stack_level = 0

        for interval in intervals:
            elements.append(Element(value=interval[0], type="open"))
            elements.append(Element(value=interval[1] + 1, type="close"))

        elements.sort(reverse=True)
        while len(elements) > 0:
            element = elements.pop()
            if element.type == "open":
                stack_level += 1
                stack.append(element)
            elif element.type == "close":
                stack_level -= 1
                element_open = stack.pop()
                element_close = element
                if stack_level == 0:
                    groups.append([
                        element_open.value,
                        element_close.value - 1,
                    ])

        return groups


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.merge(intervals=[
            [1, 3],
            [2, 6],
            [8, 10],
            [15, 18],
        ])
    )
    print(
        solution.merge(intervals=[[1, 4], [4, 5]])
    )
    print(
        solution.merge(intervals=[
            [1, 4],
            [2, 3],
        ])
    )
    print(
        solution.merge(intervals=[
            [1, 4],
            [0, 5],
        ])
    )
    print(
        solution.merge(intervals=[
            [2, 3],
            [4, 5],
            [6, 7],
            [8, 9],
            [1, 10],
        ])
    )
