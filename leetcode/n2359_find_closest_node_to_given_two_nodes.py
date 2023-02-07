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


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        reachable = defaultdict(set)
        for from_node, destination_node in enumerate(edges):
            if destination_node != -1:
                reachable[from_node].add(destination_node)

        # noinspection PyShadowingNames
        def bfs(origin_node: int):
            visited = set()
            nodes_queue = deque([(origin_node, 0)])
            distances = Counter()

            while len(nodes_queue) > 0:
                node, distance = nodes_queue.popleft()
                distances[node] = distance

                if node not in visited:
                    visited.add(node)
                    destination_nodes = [
                        destination_node
                        for destination_node in reachable[node]
                        if destination_node not in visited
                    ]
                    nodes_queue.extend(
                        (destination_node, distance + 1)
                        for destination_node in destination_nodes
                    )

            return distances

        distances_1 = bfs(origin_node=node1)
        distances_2 = bfs(origin_node=node2)
        common_nodes_with_difference = [
            (max(distances_1[node], distances_2[node]), node)
            for node in distances_1.keys()
            if node in distances_2
        ]
        if len(common_nodes_with_difference) > 0:
            common_nodes_with_difference = sorted(common_nodes_with_difference)
            return common_nodes_with_difference[0][1]

        return -1


if __name__ == '__main__':
    solution = Solution()
    # print(
    #     solution.closestMeetingNode(
    #         edges=[2, 2, 3, -1],
    #         node1=0,
    #         node2=1,
    #     )
    # )
    # print(
    #     solution.closestMeetingNode(
    #         edges=[1, 2, -1],
    #         node1=0,
    #         node2=2,
    #     )
    # )
    # print(
    #     solution.closestMeetingNode(
    #         edges=[4, 3, 0, 5, 3, -1],
    #         node1=4,
    #         node2=0,
    #     )
    # )
    print(
        solution.closestMeetingNode(
            edges=[4, 4, 8, -1, 9, 8, 4, 4, 1, 1],
            node1=5,
            node2=6,
        )
    )
