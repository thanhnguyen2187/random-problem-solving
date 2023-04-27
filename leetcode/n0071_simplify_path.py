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
    groupby,
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
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        parts = [
            part
            for part in parts
            if part != '.' and part
        ]

        def make_state_func():
            state = 'no_slash'

            def change_state(part: str):
                nonlocal state
                match (state, part):
                    case ('no_slash', '/'):
                        state = 'one_slash'
                    case ('one_slash', '/'):
                        state = 'multiple_slashes'
                    case ('multiple_slashes', '/'):
                        ...
                    case (_, _):
                        state = 'no_slash'

                return state

            return change_state

        # deduplicate consecutive slashes ('//...')
        change_state_func = make_state_func()
        parts = [
            part
            for part in parts
            if change_state_func(part) in ('one_slash', 'no_slash')
        ]

        parts_without_dotdot = []
        for part in parts:
            if part == '..':
                if parts_without_dotdot:
                    parts_without_dotdot.pop()
            else:
                parts_without_dotdot.append(part)

        result = '/'.join(parts_without_dotdot).rstrip('/')
        result = '/' + result

        return result


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.simplifyPath(path='/../')
    )
