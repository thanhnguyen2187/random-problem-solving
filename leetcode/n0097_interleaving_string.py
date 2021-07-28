from typing import (
    List,
    Optional,
    Union,
    NamedTuple,
    Dict,
    Set,
    Iterator,
)
from bisect import (
    bisect_left,
    bisect_right,
)
from itertools import (
    product,
    cycle,
    repeat,
    islice,
    chain,
    accumulate,
    takewhile,
    permutations,
)
from functools import (
    cached_property,
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

    def isInterleave(
        self,
        s1: str,
        s2: str,
        s3: str,
    ) -> bool:

        if s1 == "":
            return s2 == s3
        elif s2 == "":
            return s1 == s3
        if len(s1) + len(s2) != len(s3):
            return False

        table = [
            [
                False
                for _, _ in enumerate("_" + s1)
            ]
            for _, _ in enumerate("_" + s2)
        ]

        table[0][0] = True

        for index_1, character_1 in enumerate("_" + s1):
            table[0][index_1] = (
                character_1 == "_" or
                (
                    character_1 == s3[index_1 - 1] and
                    table[0][index_1 - 1] is True
                )
            )

        for index_2, character_2 in enumerate("_" + s2):
            table[index_2][0] = (
                character_2 == "_" or
                (
                    character_2 == s3[index_2 - 1] and
                    table[index_2 - 1][0] is True
                )
            )

        for index_2, index_1 in product(
            range(1, len(s2) + 1),
            range(1, len(s1) + 1),
        ):
            index_3 = index_1 + index_2 - 1
            table[index_2][index_1] = (
                (
                    s3[index_3] == s1[index_1 - 1] and
                    table[index_2][index_1 - 1] is True
                ) or (
                    s3[index_3] == s2[index_2 - 1] and
                    table[index_2 - 1][index_1] is True
                )
            )

        return table[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    for (
        s1, s2, s3,
    ) in [
        # ("a", "", "c",),
        ("a", "a", "aa",),
        ("db", "b", "cbb"),
        ("aabc", "abad", "aabadabc"),
        ("aabcc", "dbbca", "aadbbbaccc")
    ]:
        print(
            solution.isInterleave(
                s1=s1,
                s2=s2,
                s3=s3,
            )
        )
