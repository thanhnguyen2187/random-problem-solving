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
    count,
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


def generate_direction(m: int, n: int) -> Iterator[str]:
    match m, n:
        case 1, 1:
            ...
        case 1, _:
            yield from repeat('right', n - 1)
        case _, 1:
            yield from repeat('down', m - 1)
        case 2, 2:
            yield from ['right', 'down', 'left']
        case 2, _:
            yield from repeat('right', n - 1)
            yield 'down'
            yield from repeat('left', n - 1)
        case _, 2:
            yield 'right'
            yield from repeat('down', m - 1)
            yield 'left'
            yield from repeat('up', m - 2)
        case _, _:
            yield from repeat('right', n - 1)
            yield from repeat('down', m - 1)
            yield from repeat('left', n - 1)
            yield from repeat('up', m - 2)
            yield 'right'
            yield from generate_direction(
                m=m - 2,
                n=n - 2,
            )


def generate_next_position(
    position: (int, int),
    direction: str,
) -> (int, int):
    x, y = position
    match direction:
        case 'right':
            return x, y + 1
        case 'down':
            return x + 1, y
        case 'left':
            return x, y - 1
        case 'up':
            return x - 1, y


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        direction_iterator = generate_direction(m=n, n=n)
        positions = [(0, 0)]

        for direction in direction_iterator:
            last_position = positions[-1]
            positions.append(
                generate_next_position(
                    position=last_position,
                    direction=direction,
                )
            )

        # Another way to create the matrix that does not work:
        #
        #   matrix = list(repeat(
        #       list(repeat(0, n)),
        #       n,
        #   ))
        #
        # The reason is that `repeat` reuses the initially created `list(repeat(0, n))`,
        # which means doing an assignment to a single element is going to change the values of other
        # elements in the same column as well. For example, with `n == 3`, this statement:
        #
        #   matrix[0][0] = 0
        #
        # Result in those unwanted side effects:
        #
        #   matrix[1][0] = 0
        #   matrix[2][0] = 0
        #
        matrix = [
            list(repeat(0, n))
            for _ in range(n)
        ]
        for number, position in zip(
            count(start=1),
            positions,
        ):
            x, y = position
            matrix[x][y] = number

        return matrix


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.generateMatrix(n=3),
    )
