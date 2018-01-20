# Definition for a binary tree node.
import Queue

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        left_sub_tree = root.left
        right_sub_tree = root.right

        left_queue = Queue.Queue()
        right_queue = Queue.Queue()

        left_queue.put(left_sub_tree)
        right_queue.put(right_sub_tree)

        while left_queue.qsize() and right_queue.qsize():

            left_node = left_queue.get()
            right_node = right_queue.get()

            if left_node is None and right_node is None:
                continue

            if not (left_node and right_node):
                return False

            if left_node.val != right_node.val:
                return False

            left_queue.put(left_node.left)
            left_queue.put(left_node.right)
            right_queue.put(right_node.right)
            right_queue.put(right_node.left)

        return True


class Solution2(object):
    def isSymmetric(self, root):
        if not root:
            return True

        subtree_left = root.left
        subtree_right = root.right

        return self.subtree_symmetric(subtree_left, subtree_right)

    def subtree_symmetric(self, left_subtree, right_subtree):

        if left_subtree is None and right_subtree is None:
            return True

        if not (left_subtree and right_subtree):
            return False

        if left_subtree.val != right_subtree.val:
            return False

        if self.subtree_symmetric(left_subtree.left, right_subtree.right) and \
            self.subtree_symmetric(left_subtree.right, right_subtree.left):
            return True
        else:
            return False

