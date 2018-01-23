# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if head is None:
            return None
        if head.next is None:
            return head

        base = ListNode(None)
        base.next = head
        previous_node = base
        current_node = head

        k = 1
        while current_node:

            if k == m:
                start_base = previous_node
                node_A = current_node
                previous_node = None
            if k == n+1:
                end_base = current_node
                node_A.next = end_base
                start_base.next = previous_node

            if k >= m and k <= n:
                next_node = current_node.next
                current_node.next = previous_node

                previous_node = current_node
                current_node = next_node
            else:
                previous_node = current_node
                current_node = current_node.next

            k += 1
        if k == n+1:
            end_base = current_node
            node_A.next = end_base
            start_base.next = previous_node


        return base.next