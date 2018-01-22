# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict

class Solution(object):

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        subtree_str_counter = defaultdict(int)
        dup_subtrees = []

        def find_dup(root):
            if root is None:
                return "#"

            root_string = "{} {} {}".format(root.val, find_dup(root.left), find_dup(root.right))

            subtree_str_counter[root_string] += 1
            if subtree_str_counter[root_string] == 2:
                dup_subtrees.append(root)

            return root_string

        find_dup(root)

        return dup_subtrees


class Solution2(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        subtree_id = defaultdict()
        subtree_id.default_factory = subtree_id.__len__
        incur_counter = defaultdict(int)
        dup_subtrees = []

        def find_dup(root):
            if root is None:
                return None

            _id = subtree_id[(root.val, find_dup(root.left), find_dup(root.right))]

            incur_counter[_id] += 1

            if incur_counter[_id] == 2:
                dup_subtrees.append(root)

            return _id

        find_dup(root)

        return dup_subtrees