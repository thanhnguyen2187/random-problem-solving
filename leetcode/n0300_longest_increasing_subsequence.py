from typing import (
    List,
    NamedTuple,
    Union,
)
from itertools import (
    accumulate,
)
from bisect import (
    bisect_left,
    bisect_right,
    insort,
    insort_left,
)


class Node(NamedTuple):
    value: Union[int, float]
    children: List['Node']


class Solution:

    def add_child(
        self,
        node: Node,
        value: int,
    ):
        if node.value < value:
            marked = False
            for child in node.children:
                if child.value < value:
                    self.add_child(
                        node=child,
                        value=value,
                    )
                    marked = True
            if not marked:
                node.children.append(
                    Node(
                        value=value,
                        children=[],
                    )
                )

    def find_maximal_depth(
        self,
        node: Node,
    ) -> int:
        if len(node.children) == 0:
            return 1
        else:
            return 1 + max(
                self.find_maximal_depth(node=child)
                for child in node.children
            )

    def lengthOfLIS(
        self,
        nums: List[int],
    ) -> int:

        root = Node(
            value=float("-inf"),
            children=[],
        )

        for number in nums:
            self.add_child(
                node=root,
                value=number,
            )

        return self.find_maximal_depth(node=root) - 1



if __name__ == '__main__':
    solution = Solution()
    print(
        solution.lengthOfLIS(
            nums=[10, 9, 2, 5, 3, 7, 101, 18],
        )
    )
    print(
        solution.lengthOfLIS(
            nums=[0, 1, 0, 3, 2, 3],
        )
    )
    print(
        solution.lengthOfLIS(
            nums=[7, 7, 7, 7, 7, 7, 7],
        )
    )
    print(
        solution.lengthOfLIS(
            nums=[7, 5, 6, 2, 1, 2, 3, 4, 5, 6, 7, 8],
        )
    )

