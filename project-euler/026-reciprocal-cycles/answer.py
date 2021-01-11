import math


def is_prime(
    number: int,
) -> bool:

    smallest_divisor = next(
        (
            divisor
            # 2 <= divisor <= sqrt(number)
            for divisor in range(2, math.floor(math.sqrt(number)) + 1)
            if number % divisor == 0
        ),
        0,  # default
    )

    if smallest_divisor == 0:
        return True
    else:
        return False


def is_reptend_prime(
    number: int,
) -> bool:

    def only_last(
        conditions: list,
    ):
        return (
            all(
                not condition
                for condition in conditions[:-1]
            )
            and conditions[-1]
        )

    return (
        is_prime(number=number)
        and only_last([
            10 ** exponent % number == 1
            for exponent in range(1, number)
        ])
        # some optimization can be done for the exponentiation
        # more information here: https://mathworld.wolfram.com/FullReptendPrime.html
    )


def solve(
    # numerator: int = 1,
    max_denominator: int = 1000,
) -> int:
    reptend_primes = [
        number
        for number in range(2, max_denominator)
        if is_reptend_prime(number=number)
    ]
    print(reptend_primes)
    return max(reptend_primes)


answer = solve()
print(answer)
