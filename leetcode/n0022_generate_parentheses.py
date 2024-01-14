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
        result = set()

        def recurse(
            left_count: int,
            right_count: int,
            current: str,
        ):
            if left_count == n and right_count == n:
                result.add(current)
            elif left_count == n:
                new_current = current + (")" * (n - right_count))
                result.add(new_current)
            elif left_count == right_count:
                recurse(
                    left_count=left_count + 1,
                    right_count=right_count,
                    current=current + "(",
                )
            elif left_count > right_count:
                recurse(
                    left_count=left_count + 1,
                    right_count=right_count,
                    current=current + "(",
                )
                recurse(
                    left_count=left_count,
                    right_count=right_count + 1,
                    current=current + ")",
                )

        recurse(left_count=0, right_count=0, current="")

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(n=1))
    print(solution.generateParenthesis(n=2))
    print(solution.generateParenthesis(n=3))
    print(solution.generateParenthesis(n=4))
