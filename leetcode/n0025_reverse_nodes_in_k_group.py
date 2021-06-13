"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up
- Could you solve the problem in O(1) extra memory space?
- You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

from typing import (
    Optional,
)

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def kth_next_node(
        node: ListNode,
        k: int,
    ) -> Optional[ListNode]:

        if k == 0:
            return node
        elif node is None:
            return None
        else:
            return Solution.kth_next_node(
                node=node.next,
                k=k - 1,
            )

    @staticmethod
    def reverse_k_nodes(
        initial_node: ListNode,
        k: int,
    ) -> Optional[ListNode]:
        if k <= 1 or initial_node is None:
            return initial_node
        else:
            kth_next_node_ = Solution.kth_next_node(
                node=initial_node,
                k=k - 1,
            )
            if kth_next_node_ and kth_next_node_.next:
                # if k == 2:
                #     (
                #         first_node.next,
                #         kth_next_node_.next,
                #     ) = (
                #         kth_next_node_.next,
                #         first_node,
                #     )
                # else:
                (
                    initial_node.next,
                    initial_node.next.next,
                    kth_next_node_.next,
                    kth_next_node_.next.next,
                ) = (
                    kth_next_node_.next,
                    kth_next_node_.next.next,
                    initial_node.next,
                    initial_node.next.next,
                )
                Solution.reverse_k_nodes(
                    initial_node=initial_node.next,
                    k=k - 2
                )
                return kth_next_node_.next

    def reverseKGroup(
        self,
        head: ListNode,
        k: int,
    ) -> ListNode:
        if head:
            initial_node = ListNode(
                next=head,
            )
            next_initial_node = self.reverse_k_nodes(
                initial_node=initial_node,
                k=k,
            )
        return head
