from collections import (
    deque,
)
from typing import (
    List,
    NamedTuple,
    Literal,
)


class Force(NamedTuple):
    position: int
    direction: Literal["L", ".", "R"]
    moment: int


class Domino(NamedTuple):
    direction: Literal["L", ".", "R"]
    last_force_moment: int


class Solution:

    def pushDominoes(self, dominoes: str) -> str:
        typed_dominoes = [
            Domino(
                direction=".",
                last_force_moment=0,
            )
            for _ in dominoes
        ]

        forces = deque(
            Force(
                position=index,
                direction=domino,
                moment=0,
            )
            for index, domino in enumerate(dominoes)
            if domino in ("L", "R")
        )

        while len(forces) > 0:
            force = forces.popleft()
            if (
                0 <= force.position <= len(dominoes) - 1
            ):
                typed_domino = typed_dominoes[force.position]
                if typed_domino.direction == ".":
                    typed_dominoes[force.position] = Domino(
                        direction=force.direction,
                        last_force_moment=force.moment,
                    )
                    forces.append(
                        Force(
                            position=(
                                force.position - 1
                                if force.direction == "L"
                                else force.position + 1
                            ),
                            direction=force.direction,
                            moment=force.moment + 1,
                        )
                    )
                elif (
                    typed_domino.last_force_moment == force.moment and
                    (
                        (
                            typed_domino.direction == "R" and
                            force.direction == "L"
                        ) or (
                            typed_domino.direction == "L" and
                            force.direction == "R"
                        )
                    )
                ):
                    typed_dominoes[force.position] = Domino(
                        direction=".",
                        last_force_moment=force.moment,
                    )

        return "".join([
            typed_domino.direction
            for typed_domino in typed_dominoes
        ])


if __name__ == '__main__':
    solution = Solution()
    for dominoes in [
        "RR.L",
        ".L.R...LR..L..",
    ]:
        print(
            solution.pushDominoes(dominoes=dominoes)
        )
