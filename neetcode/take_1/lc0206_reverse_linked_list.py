from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        tail = None

        def recurse(head: ListNode):
            nonlocal tail
            if head.next is None:
                tail = head
                return

            recurse(head=head.next)

            head.next.next = head

        recurse(head=head)

        return tail


if __name__ == "__main__":
    solution = Solution()
    nodes = [
        ListNode(val=1, next=None),
        ListNode(val=2, next=None),
        ListNode(val=3, next=None),
        ListNode(val=4, next=None),
        ListNode(val=5, next=None),
    ]
    for node_1, node_2 in zip(nodes, nodes[1:]):
        node_1.next = node_2

    result = solution.reverseList(head=nodes[0])

    print(result)
