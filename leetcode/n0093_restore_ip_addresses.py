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


def is_valid_part(part: str) -> bool:
    if len(part) == 1:
        return 0 <= int(part) <= 9
    elif len(part) == 2:
        return 10 <= int(part) <= 99
    elif len(part) == 3:
        return 100 <= int(part) <= 255
    return False


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        for (
            position_1,
            position_2,
            position_3,
            position_4,
        ) in product(
            range(1, 4),
            range(1, 4),
            range(1, 4),
            range(1, 4),
        ):
            if sum((
                position_1,
                position_2,
                position_3,
                position_4,
            )) == len(s):
                positions = list(accumulate((
                    position_1,
                    position_2,
                    position_3,
                    position_4,
                )))
                number_1 = s[:positions[0]]
                number_2 = s[positions[0]:positions[1]]
                number_3 = s[positions[1]:positions[2]]
                number_4 = s[positions[2]:positions[3]]
                numbers = (
                    number_1,
                    number_2,
                    number_3,
                    number_4,
                )
                if all(map(is_valid_part, numbers)):
                    results.append('.'.join(numbers))

        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.restoreIpAddresses(s="25525511135"))
    print(solution.restoreIpAddresses(s="0000"))
    print(solution.restoreIpAddresses(s="101023"))
