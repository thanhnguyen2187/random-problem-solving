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
    cache,
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(Counter)
        n = len(tickets) + 1

        for i, j in tickets:
            graph[i][j] += 1

        results = []
        result = []
        def recurse(i: str):
            if len(results) > 0:
                return
            result.append(i)
            if len(result) == n:
                results.append(result.copy())
                return
            for j in sorted(graph[i].keys()):
                if graph[i][j] > 0:
                    graph[i][j] -= 1
                    recurse(i=j)
                    graph[i][j] += 1
            result.pop()

        recurse(i="JFK")
        return results[0]


if __name__ == '__main__':
    solution = Solution()
    # tickets = [
    #     ["MUC", "LHR"],
    #     ["JFK", "MUC"],
    #     ["SFO", "SJC"],
    #     ["LHR", "SFO"],
    # ]
    # tickets = [
    #     ["JFK", "KUL"],
    #     ["JFK", "NRT"],
    #     ["NRT", "JFK"],
    # ]
    # tickets = [
    #     ["JFK", "SFO"],
    #     ["JFK", "ATL"],
    #     ["SFO", "ATL"],
    #     ["ATL", "JFK"],
    #     ["ATL", "SFO"],
    # ]
    tickets = [
        ["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"],
        ["JFK", "ANU"], ["ANU", "EZE"], ["TIA", "ANU"],
        ["AXA", "TIA"], ["TIA", "JFK"], ["ANU", "TIA"],
        ["JFK", "TIA"]
    ]
    print(solution.findItinerary(tickets=tickets))
