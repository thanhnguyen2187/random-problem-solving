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
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        next_courses = defaultdict(list)
        indegree = Counter()

        for i, j in prerequisites:
            next_courses[j].append(i)
            indegree[i] += 1

        result = []
        def recurse(i: int):
            result.append(i)

            indegree[i] = -1
            for j in next_courses[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    recurse(j)

            return True

        for i in range(numCourses):
            if indegree[i] == 0:
                recurse(i=i)

        if len(result) != numCourses:
            return []

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findOrder(
        numCourses=2,
        prerequisites=[[1, 0], [0, 1]],
    ))
    print(solution.findOrder(
        numCourses=4,
        prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]],
    ))
    print(solution.findOrder(
        numCourses=2,
        prerequisites=[],
    ))
