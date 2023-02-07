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
    def thousandSeparator(self, n: int) -> str:
        n_str = list(reversed(str(n)))
        digit_count = 3
        chunks = [
            ''.join(n_str[index:index + digit_count])
            for index in range(0, len(n_str), digit_count)
        ]
        result = '.'.join(chunks)
        result = ''.join(reversed(result))
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.thousandSeparator(n=1000))
    print(solution.thousandSeparator(n=100000))
