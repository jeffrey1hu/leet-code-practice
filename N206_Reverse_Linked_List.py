# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head

        previous_node = None
        current_node = head

        while current_node:

            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node

        return previous_node


