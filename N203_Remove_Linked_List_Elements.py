# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None

        last_pointer = ListNode(None)
        last_pointer.next = head

        current_node = head
        previous_node = last_pointer

        while current_node.next is not None:
            next_node = current_node.next
            if current_node.val == val:
                previous_node.next = next_node
                current_node = next_node
            else:
                previous_node = current_node
                current_node = next_node
        if current_node.val == val:
            previous_node.next = None

        return last_pointer.next
