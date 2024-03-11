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
    cache,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def recurse(o: int, c: int, current: str):
            if o > n:
                return
            if o == c and o == n:
                result.append(current)
                return

            if o > c:
                recurse(o=o, c=c + 1, current=current + ')')
                recurse(o=o + 1, c=c, current=current + '(')
            elif o == c:
                recurse(o=o + 1, c=c, current=current + '(')

        recurse(o=0, c=0, current='')

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(n=1))
    print(solution.generateParenthesis(n=2))
    print(solution.generateParenthesis(n=3))
    print(solution.generateParenthesis(n=4))
