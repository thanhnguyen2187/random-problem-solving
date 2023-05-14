from typing import (
    DefaultDict,
    Dict,
    Iterator,
    List,
    NamedTuple,
    Optional,
    Set,
    Union,
)
from bisect import (
    bisect_left,
    bisect_right,
)
from itertools import (
    accumulate,
    chain,
    combinations,
    cycle,
    islice,
    permutations,
    product,
    repeat,
    takewhile,
)
from functools import (
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)
from heapq import (
    heapify,
    heappush,
    heappop,
)


def calculate_senate_state(senate: str) -> str:
    radiant_count = 0
    dire_count = 0

    for senator in senate:
        if senator == "R":
            radiant_count += 1
        elif senator == "D":
            dire_count += 1
        elif senator == " ":
            continue
        else:
            raise ValueError("calculate_senate_state unreachable code with senator = " + senator)
        if radiant_count >= 1 and dire_count >= 1:
            return "mixed"

    if dire_count == 0:
        return "all_radiant"
    elif radiant_count == 0:
        return "all_dire"
    else:
        raise ValueError("calculate_senate_state unreachable code")


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_indexes = set()
        dire_indexes = set()

        for index, senator in enumerate(senate):
            if senator == "R":
                radiant_indexes.add(index)
            elif senator == "D":
                dire_indexes.add(index)

        while (state := calculate_senate_state(senate=senate)) == "mixed":
            for index in range(len(senate)):
                match senate[index]:
                    case "R":
                        dire_index = senate.find("D", index + 1)
                        if dire_index == -1:
                            dire_index = senate.find("D", 0, index)
                        if dire_index == -1:
                            continue
                        dire_indexes.remove(dire_index)
                        senate = f"{senate[:dire_index]} {senate[dire_index + 1:]}"
                    case "D":
                        radiant_index = senate.find("R", index + 1)
                        if radiant_index == -1:
                            radiant_index = senate.find("R", 0, index)
                        if radiant_index == -1:
                            continue
                        radiant_indexes.remove(radiant_index)
                        senate = f"{senate[:radiant_index]} {senate[radiant_index + 1:]}"

        match state:
            case "all_radiant":
                return "Radiant"
            case "all_dire":
                return "Dire"


if __name__ == '__main__':
    solution = Solution()
    print(solution.predictPartyVictory(senate="RD"))
    print(solution.predictPartyVictory(senate="RDD"))
    print(solution.predictPartyVictory(senate="DDRRR"))
    print(solution.predictPartyVictory(senate="DRRDRDRDRDDRDRDR"))
