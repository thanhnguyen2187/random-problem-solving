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


class DisjointSet:
    parents: Dict
    ranks: DefaultDict

    def find(self, item):
        self.parents.setdefault(item, item)
        if item != self.parents[item]:
            self.parents[item] = self.find(self.parents[item])
        return self.parents[item]

    def union(self, *items):
        for item_1, item_2 in zip(items, items[1:]):
            parent_1 = self.find(item=item_1)
            parent_2 = self.find(item=item_2)
            if self.ranks[item_1] < self.ranks[item_2]:
                self.parents[item_1] = parent_2
                self.ranks[item_2] += 1
            else:
                self.parents[item_2] = parent_1
                self.ranks[item_1] += 1

    def __init__(self):
        self.parents = dict()
        self.ranks = defaultdict(lambda: 0)


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        tree = defaultdict(set)
        disjoint_set = DisjointSet()

        for edge in edges:
            from_, to = edge
            tree[from_].add(to)
            tree[to].add(from_)

        value_to_nodes = {
            key: tuple(map(lambda pair: pair[0], nodes))
            for key, nodes in groupby(
                sorted(enumerate(vals), key=lambda pair: pair[1]),
                key=lambda pair: pair[1],
            )
        }

        good_path_number = 0
        for value, nodes in value_to_nodes.items():
            for node in nodes:
                child_nodes = [
                    child_node
                    for child_node in tree[node]
                    if vals[child_node] <= value
                ]
                disjoint_set.find(node)
                list(map(disjoint_set.find, child_nodes))
                disjoint_set.union(node, *child_nodes)

            node_groups = defaultdict(set)
            for node, index in disjoint_set.parents.items():
                node_groups[index].add(node)

            for group_index, group_nodes in node_groups.items():
                good_path_points = [
                    node
                    for node in group_nodes
                    if node in nodes
                ]
                good_path_number += (len(good_path_points) * (len(good_path_points) + 1)) // 2

        return good_path_number


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.numberOfGoodPaths(
            vals=[1, 3, 2, 1, 3],
            edges=[[0, 1], [0, 2], [2, 3], [2, 4]],
        )
    )
    # print(
    #     solution.numberOfGoodPaths(
    #         vals=[1, 1, 2, 2, 3],
    #         edges=[[0, 1], [1, 2], [2, 3], [2, 4]],
    #     )
    # )
    print(
        solution.numberOfGoodPaths(
            vals=[2, 5, 5, 1, 5, 2, 3, 5, 1, 5],
            edges=[[0, 1], [2, 1], [3, 2], [3, 4], [3, 5], [5, 6], [1, 7], [8, 4], [9, 7]],
        )
    )
