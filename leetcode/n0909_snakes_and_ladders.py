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


def roundrobin(*iterables):
    """roundrobin('ABC', 'D', 'EF') --> A D E B F C"""
    # Recipe credited to George Sakkis
    num_active = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        # make the board a "normal" n*n one
        board = list(reversed(board))
        board = [
            (
                row
                if not reversed_
                else list(reversed(row))
            )
            for row, reversed_ in zip(
                board, roundrobin(repeat(False), repeat(True))
            )
        ]
        # flatten the board
        # pad a 0 at the beginning
        board = [0] + [
            possible_move
            for row in board
            for possible_move in row
        ]

        positions_queue = deque([(1, 0)])
        distances = defaultdict(lambda: -1)

        while len(positions_queue) > 0:
            current_position, distance = positions_queue.popleft()
            if current_position == n * n:
                return distance

            if distances[current_position] == -1:
                distances[current_position] = distance
                positions_queue.extend(
                    (
                        (
                            position
                            if board[position] == -1
                            else board[position]
                        ),
                        distance + 1,
                    )
                    for position in range(current_position + 1, current_position + 7)
                    if distances[position] == -1 and position < len(board)
                )
            ...

        return -1


if __name__ == '__main__':
    solution = Solution()
    # print(
    #     solution.snakesAndLadders(
    #         board=[
    #             [-1, -1, -1, -1, -1, -1],
    #             [-1, -1, -1, -1, -1, -1],
    #             [-1, -1, -1, -1, -1, -1],
    #             [-1, 35, -1, -1, 13, -1],
    #             [-1, -1, -1, -1, -1, -1],
    #             [-1, 15, -1, -1, -1, -1]
    #         ]
    #     )
    # )
    print(
        solution.snakesAndLadders(
            board=[
                [-1, -1, -1, 30, -1, 144, 124, 135, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 167, 93, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, 77, -1, -1, 90, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 122, -1],
                [-1, -1, -1, 23, -1, -1, -1, -1, -1, 155, -1, -1, -1],
                [-1, -1, 140, 29, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, 115, -1, -1, -1, 109, -1, -1, 5],
                [-1, 57, -1, 99, 121, -1, -1, 132, -1, -1, -1, -1, -1],
                [-1, 48, -1, -1, -1, 68, -1, -1, -1, -1, 31, -1, -1],
                [-1, 163, 147, -1, 77, -1, -1, 114, -1, -1, 80, -1, -1],
                [-1, -1, -1, -1, -1, 57, 28, -1, -1, 129, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, 87, -1, -1, -1]
            ],
        )
    )
