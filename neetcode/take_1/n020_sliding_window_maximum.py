from typing import List, Deque
from collections import deque, namedtuple

Element = namedtuple('Element', ['i', 'value'])


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq: Deque[Element] = deque()
        result = []

        for i in range(len(nums)):
            # prune queue to ensure that the elements are within the sliding window
            while len(dq) > 0 and dq[0].i <= i - k:
                dq.popleft()
            # prune queue to ensure that the elements are sorted descending
            while len(dq) > 0 and dq[-1].value < nums[i]:
                dq.pop()

            dq.append(Element(i=i, value=nums[i]))
            result.append(dq[0].value)

        return result[k - 1:]


if __name__ == "__main__":
    s = Solution()
    # nums = [1, 2, 1, 0, 4, 2, 6]
    # k = 3
    nums = [1, -1]
    k = 1
    # nums = [7, 2, 4]
    # k = 2
    result = s.maxSlidingWindow(nums=nums, k=k)
    print(result)
