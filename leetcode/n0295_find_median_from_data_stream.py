import math
from bisect import (
    insort,
)


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        insort(
            a=self.nums,
            x=num,
        )

    def findMedian(self) -> float:
        first_index = math.ceil((len(self.nums) - 1) / 2)
        second_index = math.floor((len(self.nums) - 1) / 2)
        return (self.nums[first_index] + self.nums[second_index]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(num=6)
    print(
        obj.findMedian()
    )

    obj.addNum(num=10)
    print(
        obj.findMedian()
    )

    obj.addNum(num=2)
    print(
        obj.findMedian()
    )

    obj.addNum(num=6)
    print(
        obj.findMedian()
    )

    obj.addNum(num=5)
    print(
        obj.findMedian()
    )

    obj.addNum(num=0)
    print(
        obj.findMedian()
    )

    obj.addNum(num=6)
    print(
        obj.findMedian()
    )

    obj.addNum(num=3)
    print(
        obj.findMedian()
    )

    obj.addNum(num=1)
    print(
        obj.findMedian()
    )

    obj.addNum(num=0)
    print(
        obj.findMedian()
    )

    obj.addNum(num=0)
    print(
        obj.findMedian()
    )
