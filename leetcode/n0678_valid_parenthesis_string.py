import heapq

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


def rindex(lst, item):
    for i in range(0, len(lst), -1):
        if lst[i] == item:
            return i

    return -1


class Solution:
    def checkValidString(self, s: str) -> bool:
        opens = []
        stars = []
        if s[0] == '(':
            opens.append(0)
        elif s[0] == ')':
            return False
        else:
            stars.append(0)

        for i in range(1, len(s)):
            char = s[i]
            if char == ')':
                if len(opens) > 0:
                    opens.pop()
                elif len(stars) > 0:
                    stars.pop()
                else:
                    return False
            elif char == '*':
                stars.append(i)
            else: # char == '('
                opens.append(i)

        while len(opens) > 0 and len(stars) > 0:
            l, r = opens.pop(), stars.pop()
            if l > r:
                return False

        return len(opens) == 0



if __name__ == '__main__':
    solution = Solution()
    # print(solution.checkValidString(s="()"))
    # print(solution.checkValidString(s="(*)"))
    # print(solution.checkValidString(s="(*"))
    # print(solution.checkValidString(s="(**"))
    # print(solution.checkValidString(s="**"))
    # print(solution.checkValidString(s=")"))
    # print(solution.checkValidString(s=")("))
    # print(solution.checkValidString(s="((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))
    print(solution.checkValidString(s="(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
    # print(solution.checkValidString(s="(*))"))
