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
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        graph = defaultdict(set)

        for i in range(n):
            graph[i].update(range(i + 1, i + nums[i] + 1))

        visited = set()
        dq = deque([(0, 0)])
        while len(dq) > 0:
            top, level = dq.popleft()
            if top in visited:
                continue
            if top >= n - 1:
                return level

            visited.add(top)
            dq.extend((
                (next_, level + 1)
                for next_ in graph[top]
            ))


if __name__ == '__main__':
    solution = Solution()
    print(solution.jump(nums=[2, 3, 1, 1, 4]))
    print(solution.jump(nums=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]))
