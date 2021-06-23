from typing import (
    List,
)


class Solution:

    def next_permutation(
        self,
        numbers: List[int],
    ):
        temporaries = [0]
        while temporaries[-1] < numbers[-1]:
            temporaries.append(numbers.pop())

        index_swap = next(
            index
            for index, temporary in enumerate(temporaries)
            if temporary > numbers[-1]
        )
        numbers[-1], temporaries[index_swap] = temporaries[index_swap], numbers[-1]
        numbers.extend(temporaries[1:])


    def getPermutation(self, n: int, k: int) -> str:
        numbers = [
            x
            for x in range(1, n + 1)
        ]

        while k > 1:
            self.next_permutation(numbers=numbers)
            k -= 1

        return "".join(
            str(number)
            for number in numbers
        )


if __name__ == "__main__":
    solution = Solution()
    print(solution.getPermutation(n=3, k=3))
    print(solution.getPermutation(n=4, k=9))
    print(solution.getPermutation(n=3, k=1))
