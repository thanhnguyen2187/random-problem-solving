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


class Block(NamedTuple):
    x: int
    y: int
    distance: int


class Solution:

    def updateMatrix(
        self,
        mat: List[List[int]],
    ) -> List[List[int]]:

        width = len(mat[0])
        height = len(mat)

        distances = [
            [
                float("inf")
                for _ in range(width)
            ]
            for _ in range(height)
        ]

        block_queue = deque(
            Block(
                x=x,
                y=y,
                distance=0,
            )
            for x, y in product(
                range(width),
                range(height),
            )
            if mat[y][x] == 0
        )

        while len(block_queue) != 0:
            block = block_queue.popleft()
            distances[block.y][block.x] = min(
                block.distance,
                distances[block.y][block.x],
            )

            for x_next, y_next in (
                (block.x - 1, block.y),
                (block.x + 1, block.y),
                (block.x, block.y - 1),
                (block.x, block.y + 1),
            ):
                if (
                    0 <= x_next < width and
                    0 <= y_next < height and
                    math.isinf(distances[y_next][x_next])
                ):
                    block_new = Block(
                        x=x_next,
                        y=y_next,
                        distance=block.distance + 1,
                    )
                    block_queue.append(block_new)

        return distances


if __name__ == '__main__':
    solution = Solution()
    for mat in (
        (
            (0, 0, 0,),
            (0, 1, 0,),
            (0, 0, 0,),
        ),
    ):
        print(
            solution.updateMatrix(mat=mat)
        )
