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
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        o = image[sr][sc]
        if o == color:
            return image

        dq = deque([(sr, sc)])
        while len(dq) > 0:
            i, j = dq.pop()
            if image[i][j] != o:
                continue

            image[i][j] = color
            for k, l in (
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
            ):
                if (
                    0 <= k < m and
                    0 <= l < n and
                    image[k][l] == o
                ):
                    dq.append((k, l))

        return image


if __name__ == '__main__':
    solution = Solution()
