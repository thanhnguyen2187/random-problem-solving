from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        slow, fast = head, head

        while (
            fast is not None and
            fast.next is not None
        ):
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == "__main__":
    solution = Solution()
    nums = []
    result = solution.solution(nums=nums)
    print(result)
