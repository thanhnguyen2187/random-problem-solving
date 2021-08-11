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
)


class ListNode:
    def __init__(
            self,
            x: int,
            next: Optional['ListNode'] = None,
    ):
        self.val: int = x
        self.next: 'ListNode' = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: 'TreeNode' = None,
        right: 'TreeNode' = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minFlipsMonoIncr(
        self,
        s: str,
    ) -> int:

        counting_dict: DefaultDict[str, List] = defaultdict(list)

        for previous_character, character in zip(
            " " + s,
            s,
        ):
            if previous_character != character:
                counting_dict[character].append(1)
            else:
                counting_dict[character][-1] += 1

        zeroes = counting_dict["0"]
        ones = counting_dict["1"]

        if s[0] == "0":
            ones.insert(0, 0)
        if s[-1] == "1":
            zeroes.append(0)

        sums = [
            sum(
                chain(
                    ones[:index],
                    zeroes[index:],
                    # chain(
                    #     zeroes[:index],
                    #     ones[index:],
                    # )
                )
            )
            for index in range(len(ones) + 1)
        ]

        return min(sums)


if __name__ == '__main__':
    solution = Solution()
    for s in [
        "00011000",
        "1010111010101000101",
        "101010100010101000101111110101111010",
        "1000001011111111010",
        "00110",
    ]:
        print(
            solution.minFlipsMonoIncr(s=s)
        )
