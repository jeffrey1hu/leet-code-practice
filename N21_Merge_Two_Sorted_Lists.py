# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        base_merge = ListNode(None)
        # base_l1 = ListNode(None)
        # base_l2 = ListNode(None)
        # base_l1.next = l1
        # l1 = base_l1
        # base_l2.next = l2
        # l2 = base_l2

        head = base_merge

        while l1 and l2:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1:
            head.next = l1
        else:
            head.next = l2
        return base_merge.next



