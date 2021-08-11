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


class Solution:

    def traverse(
        self,
        found_paths: List[List[int]],
        current_node: TreeNode,
        current_path: List[int],
        remains: int,
    ):
        if (
            current_node is None
        ):
            return

        current_path.append(current_node.val)
        remains -= current_node.val

        if (
            remains == 0 and
            current_node.left is None and
            current_node.right is None
        ):
            found_paths.append(current_path.copy())
        else:
            for next_node in (
                current_node.left,
                current_node.right,
            ):
                self.traverse(
                    found_paths=found_paths,
                    current_node=next_node,
                    current_path=current_path,
                    remains=remains,
                )

        remains += current_node.val
        current_path.pop()

    def pathSum(
        self,
        root: TreeNode,
        targetSum: int,
    ) -> List[List[int]]:

        found_paths = []
        self.traverse(
            found_paths=found_paths,
            current_node=root,
            current_path=[],
            remains=targetSum,
        )
        return found_paths


def create_tree(
    values: List[int],
    index: int,
) -> Optional[TreeNode]:

    if (
        index < len(values) and
        values[index] is not None
    ):
        root = TreeNode(val=values[index])
        root.left = create_tree(
            values=values,
            index=index*2 + 1
        )
        root.right = create_tree(
            values=values,
            index=index*2 + 2
        )
        return root


if __name__ == '__main__':
    solution = Solution()
    for root_list, target_sum in [
        (
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1],
            22,
        ),
        (
            [],
            1,
        ),
        (
            [-2, None, -3],
            -5,
        )
    ]:
        root = create_tree(
            values=root_list,
            index=0,
        )
        print(
            solution.pathSum(root=root, targetSum=target_sum)
        )
