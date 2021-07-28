import string
from typing import (
    List,
    Optional,
    Union,
    NamedTuple,
    Dict,
    Set,
)
from bisect import (
    bisect_left,
    bisect_right,
)
from itertools import (
    product,
    cycle,
    repeat,
    islice,
    chain,
    accumulate,
    takewhile,
    permutations,
)
from functools import (
    cached_property,
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

    val: int
    left: 'TreeNode'
    right: 'TreeNode'

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

    def tree_insert(
        self,
        element: int,
        tree: Dict[int, int],
    ):

        index = 0
        inserted = False

        while inserted is False:
            if tree.get(index) is None:
                tree[index] = element
                inserted = True
            elif element < tree[index]:
                index = index * 2 + 1
            else:
                index = index * 2 + 2

    def tree_create(
        self,
        tree_str: str,
    ) -> TreeNode:
        tree_dict: Dict[int, TreeNode] = {
            index: TreeNode(val=int(character))
            for index, character in enumerate(tree_str)
            if character in string.digits
        }

        for index in range(len(tree_str)):
            child_left_index = index * 2 + 1
            child_right_index = index * 2 + 2
            if tree_dict.get(index) is not None:
                tree_dict[index].left = tree_dict.get(child_left_index)
                tree_dict[index].right = tree_dict.get(child_right_index)

        return tree_dict[0]

    def generateTrees(
        self,
        n: int,
    ) -> List[TreeNode]:

        elements = [
            element + 1
            for element in range(n)
        ]
        trees_saved = set()

        for permutation in permutations(elements):
            tree = {}
            list(
                map(
                    lambda element: self.tree_insert(element=element, tree=tree),
                    permutation,
                )
            )
            tree_length = max(tree)
            trees_saved.add(
                "".join(
                    str(tree.get(key, "-"))
                    for key in range(tree_length + 1)
                )
            )

        return [
            self.tree_create(tree_str=tree_str)
            for tree_str in trees_saved
        ]


if __name__ == '__main__':
    solution = Solution()
    for n in [
        1, 2, 3, 4,
    ]:
        print(
            solution.generateTrees(n=n)
        )
