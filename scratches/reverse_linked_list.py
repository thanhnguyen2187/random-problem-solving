from typing import (
    List,
    Optional,
)


class Node:
    value: int
    next: Optional['Node']

    def __init__(
        self,
        value: int,
        next: Optional['Node'] = None,
    ):
        self.value = value
        self.next = next


def reverse(
    head: Node,
) -> Node:

    if head.next is None:
        return head

    last = reverse(head=head.next)
    head.next.next = head
    head.next = None

    return last


def reverse_n_nodes(
    head: Node,
    n: int,
) -> Node:

    if n == 1:
        return head

    tail = reverse_n_nodes(head=head.next, n=n - 1)
    temp = head.next.next
    head.next.next = head
    head.next = temp

    return tail


def print_(
    head: Node,
):
    while head is not None:
        print(head.value)
        head = head.next


if __name__ == '__main__':
    head = Node(
        value=1,
        next=Node(
            value=2,
            next=Node(
                value=3,
                next=Node(
                    value=4,
                )
            )
        )
    )
    print_(head=head)

    # print("*" * 20)
    # head = reverse(head=head)
    # print_(head=head)

    print("*" * 20)
    head = reverse_n_nodes(head=head, n=3)
    print_(head=head)
