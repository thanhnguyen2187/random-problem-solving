from itertools import (
    accumulate,
    product,
)
from bisect import (
    insort,
    bisect_left,
    bisect_right,
)
from typing import (
    List,
)


def find_version_1(
    array: List[int],
    k: int,
) -> int:
    sums_accumulated = [0] + list(accumulate(array))
    array_length = len(sums_accumulated)

    sum_max_encountered = float("-inf")
    for left_index in range(array_length):
        for right_index in range(left_index + 1, array_length):
            sum_left = sums_accumulated[left_index]
            sum_right = sums_accumulated[right_index]

            sum_current = sum_right - sum_left
            if (
                sum_max_encountered < sum_current <= k
            ):
                sum_max_encountered = sum_current

    return sum_max_encountered


def find_version_2(
    array: List[int],
    k: int,
) -> int:

    array_length = len(array)
    sums_accumulated = list(accumulate(array))
    sums_encountered = [0]
    sum_max = min(array)

    for sum_right in sums_accumulated:
        target = sum_right - k
        sum_left_index = bisect_left(
            a=sums_encountered,
            x=target,
        )

        if sum_left_index < len(sums_encountered):
            sum_left = sums_encountered[sum_left_index]
            sum_current = sum_right - sum_left
            if sum_current <= k:
                sum_max = max(
                    sum_max,
                    sum_current,
                )

        insort(
            a=sums_encountered,
            x=sum_right,
        )

    return sum_max


if __name__ == "__main__":

    for function_ in [
        find_version_1,
        find_version_2,
    ]:
        print(
            function_(
                array=[
                    6, -2, 3
                ],
                k=4,
            )
        )
        print(
            function_(
                array=[
                    4, 8, 6,
                ],
                k=3,
            )
        )
        print("*" * 20)
