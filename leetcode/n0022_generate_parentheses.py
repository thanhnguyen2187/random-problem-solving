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


def generate(
    left_count: int,
    right_count: int,
    current: str,
    result: Set,
):
    if left_count == 0 and right_count == 0:
        result.add(current)
    elif left_count == 0:
        generate(
            left_count=0,
            right_count=0,
            current=current + (")" * right_count),
            result=result,
        )
    elif left_count == right_count:
        for new_current in {
            current + "(",
            "(" + current,
        }:
            generate(
                left_count=left_count - 1,
                right_count=right_count,
                current=new_current,
                result=result,
            )
    elif left_count > right_count:
        for new_current in {
            current + "(",
            "(" + current,
        }:
            generate(
                left_count=left_count - 1,
                right_count=right_count,
                current=new_current,
                result=result,
            )
        generate(
            left_count=left_count,
            right_count=right_count - 1,
            current=current + ")",
            result=result,
        )
    elif left_count < right_count:
        generate(
            left_count=left_count - 1,
            right_count=right_count,
            current="(" + current,
            result=result,
        )


#
# (
# () ((



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = set()
        generate(left_count=n, right_count=n, result=result, current="")

        return result


if __name__ == '__main__':
    solution = Solution()
    # print(solution.generateParenthesis(n=1))
    print(solution.generateParenthesis(n=2))
    # print(solution.generateParenthesis(n=3))
    # print(solution.generateParenthesis(n=4))
