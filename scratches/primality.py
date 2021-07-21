from math import (
    isqrt,
)


def is_prime_naive(x: int) -> bool:
    return (
        x > 1 and
        not any(
            x % factor == 0
            for factor in range(2, x)
        )
    )


def is_prime_better(x: int) -> bool:
    return (
        x > 1 and
        x % 2 != 0 and
        not any(
            x % factor == 0
            for factor in range(3, isqrt(x), 2)
        )
    )


if __name__ == "__main__":

    for is_prime_function in (
        is_prime_naive,
        is_prime_better,
    ):
        assert is_prime_function(3) is True
        assert is_prime_function(4) is False
        assert is_prime_function(5) is True
        assert is_prime_function(6) is False


