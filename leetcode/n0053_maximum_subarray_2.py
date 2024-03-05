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
    def maxSubArray(self, nums: List[int]) -> int:

        accumulated = [0]
        result = nums[0]
        for num in nums:
            accumulated.append(max(num, accumulated[-1] + num))
            result = max(result, accumulated[-1])

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray(nums=[1, 2, -1]))
    print(solution.maxSubArray(nums=[-2, -1]))
    print(solution.maxSubArray(nums=[-2]))
    print(solution.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))
    print(solution.maxSubArray(nums=[5,4,-1,7,8]))
