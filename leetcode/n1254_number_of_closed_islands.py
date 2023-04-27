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
    groupby,
)
from functools import (
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


def find_surround_slots(x: int, y: int, m: int, n: int):
    return [
        (i, j)
        for i, j in [
            (x - 1, y),
            (x, y - 1),
            (x + 1, y),
            (x, y + 1),
        ]
        if 0 <= i < m and 0 <= j < n
    ]


def is_edge_slot(x: int, y: int, m: int, n: int):
    return (
        (x == 0 or x == m - 1)
        or (y == 0 or y == n - 1)
    )


def any_edge_slot(slots: [(int, int)], m: int, n: int):
    return any(
        is_edge_slot(x=x, y=y, m=m, n=n)
        for x, y in slots
    )


class DisjointSet:
    tracker: DefaultDict

    def find(self, *items) -> bool:
        return all([
            self.tracker[item_1] == self.tracker[item_2]
            for item_1, item_2 in zip(items, items[1:])
        ])

    def union(self, *items):
        indexes = {
            self.tracker[item]
            for item in items
        }
        min_index = min(indexes)
        for item in self.tracker.keys():
            if self.tracker[item] in indexes:
                self.tracker[item] = min_index

    def __init__(self):
        self.tracker = defaultdict(lambda: len(self.tracker))


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        disjoint_set = DisjointSet()
        m = len(grid)
        n = len(grid[0])
        for x, y in product(range(m), range(n)):
            if grid[x][y] == 0:
                slots = find_surround_slots(x=x, y=y, m=m, n=n)
                land_slots = [
                    (i, j)
                    for i, j in slots
                    if grid[i][j] == 0
                ]
                disjoint_set.union((x, y), *land_slots)

        group_id_to_slots = defaultdict(list)
        for slot, group_id in disjoint_set.tracker.items():
            group_id_to_slots[group_id].append(slot)

        result = sum(
            1
            if not any_edge_slot(slots=slots, m=m, n=n)
            else 0
            for slots in group_id_to_slots.values()
        )
        return result


if __name__ == '__main__':
    solution = Solution()
    # print(solution.closedIsland(
    #     grid=[
    #         [1, 1, 1, 1, 1, 1, 1],
    #         [1, 0, 0, 0, 0, 0, 1],
    #         [1, 0, 1, 1, 1, 0, 1],
    #         [1, 0, 1, 0, 1, 0, 1],
    #         [1, 0, 1, 1, 1, 0, 1],
    #         [1, 0, 0, 0, 0, 0, 1],
    #         [1, 1, 1, 1, 1, 1, 1]
    #     ],
    # ))
    # print(solution.closedIsland(
    #     grid=[
    #         [1, 1, 1, 1, 1, 1, 1, 0],
    #         [1, 0, 0, 0, 0, 1, 1, 0],
    #         [1, 0, 1, 0, 1, 1, 1, 0],
    #         [1, 0, 0, 0, 0, 1, 0, 1],
    #         [1, 1, 1, 1, 1, 1, 1, 0],
    #     ],
    # ))
    print(solution.closedIsland(
        grid=[
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        ],
    ))
    # [[1, 1, 1, 1, 1, 1],
    #  [1, 1, 0, 1, 0, 1],
    #  [1, 0, 1, 0, 1, 1],
    #  [1, 1, 0, 0, 1, 1],
    #  [1, 1, 1, 1, 1, 1],
    #  [1, 0, 0, 0, 0, 1]]
