
# Definition for singly-linked list.
class ListNode:
    def __init__(
        self,
        val: int = 0,
        next: 'ListNode' = None,
    ):
        self.val = val
        self.next = next


class Solution:

    def delete_duplicates(
        self,
        head: ListNode,
    ) -> (
        ListNode,
        int,
    ):

        if (
            head.next is None
        ):
            return head, 1

        node, counter = self.delete_duplicates(head=head.next)
        if node.next is None:
            pass
        elif node.val == node.next.val:
            node.next = node.next.next
            counter += 1
        elif node.val != node.next.val and counter > 1:
            node.next = node.next.next
            counter = 1
        # elif counter == 1:
        #     pass

        return head, counter

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        first = ListNode(
            val=-101,
            next=head,
        )
        _, counter = self.delete_duplicates(head=first)
        if counter > 1:
            first.next = first.next.next
        return first.next


def print_(head: ListNode):
    if head is not None:
        print(head.val)
        print_(head.next)


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=2,
                    next=ListNode(
                        val=2,
                        next=ListNode(
                            val=4,
                        )
                    )
                )
            )
        )
    )
    head = solution.deleteDuplicates(head=head)
    print_(head=head)
