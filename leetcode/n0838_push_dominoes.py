import copy
import dataclasses
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

class Domino:
    direction: Literal["L", ".", "R"]
    last_force_moment: int

    def __init__(
        self,
        direction: Literal["L", ".", "R"],
        last_force_moment: int,
    ):
        self.direction = direction
        self.last_force_moment = last_force_moment


class Solution:

    def pushDominoes(self, dominoes: str) -> str:

        typed_dominoes = [
            Domino(
                direction=domino,
                last_force_moment=0,
            )
            for domino in dominoes
        ]

        forces = deque(
            Force(
                position=(
                    index - 1
                    if domino == "L"
                    else index + 1
                ),
                direction=domino,
                moment=0,
            )
            for index, domino in enumerate(dominoes)
            if domino in ("L", "R")
        )

        while len(forces) != 0:
            force = forces.popleft()
            if (
                0 <= force.position <= len(dominoes) - 1
            ):
                typed_domino = typed_dominoes[force.position]
                if typed_domino.direction == ".":
                    typed_domino.direction = force.direction
                    typed_domino.last_force_moment = force.moment
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
                    typed_domino.direction == "L" and
                    typed_domino.last_force_moment == force.moment and
                    force.direction == "R"
                ):
                    typed_domino.direction = "."
                elif (
                    typed_domino.direction == "R" and
                    typed_domino.last_force_moment == force.moment and
                    force.direction == "L"
                ):
                    typed_domino.direction = "."

