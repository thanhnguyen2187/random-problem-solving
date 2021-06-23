from typing import (
    List,
)
from itertools import (
    zip_longest,
)


class Solution:

    def addBinary(self, a: str, b: str) -> str:

        carry = "0"
        c = ""
        for pair in zip_longest(
            reversed(a),
            reversed(b),
            fillvalue="0",
        ):
            if (
                (pair[0] == "0" and pair[1] == "0" and carry == "0")
            ):
                c += "0"
            elif (
                (pair[0] == "0" and pair[1] == "0" and carry == "1")
            ):
                c += "1"
                carry = "0"
            elif (
                (pair[0] == "0" and pair[1] == "1" and carry == "0") or
                (pair[0] == "1" and pair[1] == "0" and carry == "0")
            ):
                c += "1"
            elif (
                (pair[0] == "0" and pair[1] == "1" and carry == "1") or
                (pair[0] == "1" and pair[1] == "0" and carry == "1")
            ):
                c += "0"
                carry = "1"
            elif (
                (pair[0] == "1" and pair[1] == "1" and carry == "0")
            ):
                c += "0"
                carry = "1"
            elif (
                (pair[0] == "1" and pair[1] == "1" and carry == "1")
            ):
                c += "1"

        if carry == "1":
            c += "1"

        return "".join(reversed(c))


if __name__ == '__main__':
    solution = Solution()
    # print(solution.addBinary(a="100", b="101"))
    print(solution.addBinary(a="11", b="1"))
