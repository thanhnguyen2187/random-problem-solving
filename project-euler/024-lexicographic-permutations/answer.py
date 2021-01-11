""" A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import typing


def factorial(n: int):
    if n <= 1:
        return 1
    else:
        return n * factorial(n=n - 1)


# TODO: write a "cleaner" function
def solve(n: int) -> str:
    digits = [
        str(digit)
        for digit in range(0, 10)
    ]  # ["0", "1", "2", ...]

    def f(
        n: int,
        digits: typing.List[str],
    ) -> str:
        if not digits:
            return ""
        else:
            a = factorial(n=len(digits) - 1)
            b = n // a
            c = n % a
            remained_digits = digits[:b] + digits[b + 1:]

            return (
                digits[b]
                + f(
                    n=c,
                    digits=remained_digits,
                )
            )

    answer = f(
        n=n,
        digits=digits,
    )
    return answer


answer = solve(1_000_000 - 1)
print(answer)
