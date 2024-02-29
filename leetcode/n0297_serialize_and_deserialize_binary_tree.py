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
    cache,
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


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


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        def recurse(root: Optional[TreeNode]):
            nonlocal result
            if root is None:
                result.append('N')
                return

            result.append(str(root.val))
            recurse(root.left)
            recurse(root.right)

        recurse(root=root)

        return ','.join(result)


    def deserialize(self, data: str) -> Optional[TreeNode]:
        node_strs = data.split(',')
        i = 0
        def recurse() -> Optional[TreeNode]:
            nonlocal i
            if node_strs[i] == 'N':
                i += 1
                return None

            node_value = int(node_strs[i])
            i += 1

            node = TreeNode(val=node_value)
            node.left = recurse()
            node.right = recurse()
            return node

        return recurse()


if __name__ == '__main__':
    codec = Codec()
    nodes = [
        TreeNode(1),
        TreeNode(2),
        TreeNode(3),
        None,
        None,
        TreeNode(4),
        TreeNode(5),
        # None,
        # None,
        # None,
        # None,
        # TreeNode(6),
        # TreeNode(7),
    ]
    for i in range(len(nodes)):
        l = 2 * i + 1
        r = 2 * i + 2
        if nodes[i] is None:
            continue
        nodes[i].left = (
            nodes[l]
            if l < len(nodes)
            else None
        )
        nodes[i].right = (
            nodes[r]
            if r < len(nodes)
            else None
        )

    # depth = recurse_depth(root=nodes[0])
    # result = codec.serialize(root=nodes[0])
    result = codec.serialize(root=None)
    # result = codec.deserialize(result)
    # result = codec.deserialize('')
    print(result)
