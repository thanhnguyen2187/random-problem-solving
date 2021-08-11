from typing import (
    DefaultDict,
    Deque,
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
)


class ListNode:
    def __init__(
            self,
            x: int,
            next: Optional['ListNode'] = None,
    ):
        self.val: int = x
        self.next: 'ListNode' = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: 'TreeNode' = None,
        right: 'TreeNode' = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Cell(NamedTuple):
    x: int
    y: int


def find_adjacent_cells(
    cell: Cell,
    n: int,
) -> List[Cell]:
    return [
        Cell(x=x, y=y)
        for x, y in [
            (cell.x + 1, cell.y),
            (cell.x - 1, cell.y),
            (cell.x, cell.y + 1),
            (cell.x, cell.y - 1),
        ]
        if (
            0 <= x < n and
            0 <= y < n
        )
    ]


class Island:
    land_cells: Set[Cell] = set()
    surround_cells: Set[Cell] = set()
    n: int

    def add_land_cell(
        self,
        cell: Cell,
    ):
        self.land_cells.add(cell)
        self.surround_cells.update(
            surround_cell
            for surround_cell in find_adjacent_cells(
                cell=cell,
                n=self.n,
            )
            if surround_cell not in self.land_cells
        )

    def get_area(
        self,
    ):
        return len(self.land_cells)

    def __init__(
        self,
        n: int,
    ):
        self.n = n


class Islands:

    islands: List[Island] = []
    n: int

    def merge_island(
        self,
        island_indices: List[int],
    ):
        ...

    def add_land_cell(
        self,
        cell: Cell,
    ):
        island = next(
            (
                island
                for island in self.islands
                if cell in island.surround_cells
            ),
            default=Island(n=self.n)
        )
        found = False
        for island in self.islands:
            if cell in island.surround_cells:
                found = True
                island.add_land_cell(cell=cell)
                break

        if not found:
            new_island = Island(n=self.n)
            new_island.add_land_cell(cell=cell)
            self.islands.append(new_island)

    def find_surround_islands(
        self,
        cell: Cell,
    ) -> List[Island]:
        return list(
            filter(
                lambda island: cell in island.surround_cells,
                self.islands,
            )
        )

    def get_island_areas(
        self,
    ) -> List[int]:
        return list(
            map(
                lambda island: island.get_area(),
                self.islands,
            )
        )

    def get_potential_areas(
        self,
        cells: List[Cell],
    ) -> List[int]:

        potential_areas = []
        for cell in cells:
            adjacent_cells = find_adjacent_cells(
                cell=cell,
                n=self.n,
            )
            connectable_islands = [
                island
                for island in self.islands
                if any(
                    adjacent_cell in island.surround_cells
                    for adjacent_cell in adjacent_cells
                )
            ]
            potential_areas.append(
                1 + sum(
                    map(
                        lambda island: island.get_area(),
                        connectable_islands,
                    )
                )
            )

        return potential_areas

    def __init__(
        self,
        n: int,
    ):
        self.n = n


class Solution:

    def largestIsland(
        self,
        grid: List[List[int]],
    ) -> int:
        n = len(grid)
        islands = Islands(n=n)

        island_cells = []
        sea_cells = []
        for x, y in product(
            range(n),
            repeat=2,
        ):
            cell = Cell(x=x, y=y)
            if grid[x][y] == 1:
                island_cells.append(cell)
            else:
                sea_cells.append(cell)

        for island_cell in island_cells:
            islands.add_land_cell(cell=island_cell)

        return max(
            *islands.get_island_areas(),
            *islands.get_potential_areas(cells=sea_cells),
        )


if __name__ == '__main__':
    solution = Solution()
    for grid in [
        [
            [1, 0],
            [0, 1],
        ],
        # [
        #     [1, 1],
        #     [0, 1],
        # ],
        # [
        #     [1, 1, 1],
        #     [0, 1, 0],
        #     [1, 1, 0],
        # ],
    ]:
        print(
            solution.largestIsland(grid=grid)
        )
