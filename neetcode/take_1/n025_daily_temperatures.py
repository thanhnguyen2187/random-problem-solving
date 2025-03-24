from typing import List
from collections import defaultdict


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result_dict = defaultdict(lambda: 0)

        for i in range(len(temperatures)):
            t = temperatures[i]
            while len(stack) > 0 and temperatures[stack[-1]] < t:
                j = stack.pop()
                result_dict[j] = i - j
            stack.append(i)

        result_list = [
            result_dict[i]
            for i in range(len(temperatures))
        ]

        return result_list


if __name__ == "__main__":
    solution = Solution()
    temperatures = [30, 38, 30, 36, 35, 40, 28]
    result = solution.dailyTemperatures(temperatures=temperatures)
    print(result)
