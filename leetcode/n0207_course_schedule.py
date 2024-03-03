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


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        next_indices = defaultdict(list)

        for i, j in prerequisites:
            next_indices[i].append(j)

        def is_cyclic(i: int, visited: list):
            if visited[i] is True:
                return True
            if len(next_indices[i]) == 0:
                return False

            visited[i] = True
            for j in next_indices[i]:
                if is_cyclic(i=j, visited=visited):
                    return True
            visited[i] = False
            next_indices[i] = []

            return False

        for i in range(numCourses):
            visited = list(repeat(0, numCourses + 1))
            if is_cyclic(i=i, visited=visited):
                return False

        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(
        numCourses=5,
        prerequisites=[[1, 4], [2, 4], [3, 1], [3, 2]],
    ))
    print(solution.canFinish(
        numCourses=1,
        prerequisites=[[0, 1], [1, 0]],
    ))
