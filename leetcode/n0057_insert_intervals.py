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

    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int],
    ) -> List[List[int]]:

        groups: List[List[int]] = []
        elements: List[Element] = []
        stack: List[Element] = []
        stack_level = 0

        for interval in [*intervals, newInterval]:
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
        solution.insert(
            intervals=[
                [1, 3],
                [6, 9],
            ],
            newInterval=[2, 5],
        )
    )
    print(
        solution.insert(
            intervals=[
                [1, 2],
                [3, 5],
                [6, 7],
                [8, 10],
                [12, 16],
            ],
            newInterval=[4, 8],
        )
    )
    print(
        solution.insert(
            intervals=[],
            newInterval=[5, 7],
        )
    )
    print(
        solution.insert(
            intervals=[
                [1, 5],
            ],
            newInterval=[2, 7],
        )
    )
