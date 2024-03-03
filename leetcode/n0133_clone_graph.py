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


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        if root is None:
            return None

        equivalent_dict = {}
        def recurse(node: 'Node'):
            if node in equivalent_dict:
                return equivalent_dict[node]

            cloned = Node(val=node.val)
            equivalent_dict[node] = cloned
            for neighbor in node.neighbors:
                cloned.neighbors.append(recurse(neighbor))
            return cloned

        return recurse(node=root)


if __name__ == '__main__':
    solution = Solution()
    nodes = [
        Node(val=0, neighbors=[]),
        Node(val=1, neighbors=[]),
        Node(val=2, neighbors=[]),
        Node(val=3, neighbors=[]),
        Node(val=4, neighbors=[]),
    ]
    # nodes[1].neighbors.append(nodes[2])
    # nodes[1].neighbors.append(nodes[4])
    # nodes[2].neighbors.append(nodes[1])
    # nodes[2].neighbors.append(nodes[3])
    # nodes[3].neighbors.append(nodes[2])
    # nodes[3].neighbors.append(nodes[4])
    # nodes[4].neighbors.append(nodes[1])
    # nodes[4].neighbors.append(nodes[3])
    # solution.cloneGraph(root=nodes[1])
    nodes[0].neighbors.append(nodes[1])
    nodes[0].neighbors.append(nodes[2])
    nodes[1].neighbors.append(nodes[0])
    nodes[1].neighbors.append(nodes[2])
    nodes[2].neighbors.append(nodes[0])
    nodes[2].neighbors.append(nodes[1])
    result = solution.cloneGraph(root=nodes[0])
    print(result)
