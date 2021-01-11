from functools import (
    lru_cache,
)
from itertools import (
    count,
)


@lru_cache
def calculate_fibonacci_number(index: int):
    if index <= 2:
        return 1
    else:
        return (
            calculate_fibonacci_number(index - 1)
            + calculate_fibonacci_number(index - 2)
        )


limit = 10 ** 999  # 10^999 has 1 000 digits
index = next(
    number
    for number in count(start=2)
    if calculate_fibonacci_number(index=number) >= limit
)

print(index)
# print(calculate_fibonacci_number(index=index))
