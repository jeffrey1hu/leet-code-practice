# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        longest_edge, longest_dia = self.scan_subtree(root)

        return max(longest_edge, longest_dia)

    def scan_subtree(self, root):
        left_longest_edge, left_diameter, right_longest_edge, right_diameter = 0, 0, 0, 0
        if root.left:
            left_longest_edge, left_diameter = self.scan_subtree(root.left)
            left_longest_edge += 1
        if root.right:
            right_longest_edge, right_diameter = self.scan_subtree(root.right)
            right_longest_edge += 1

        root_diameter = left_longest_edge + right_longest_edge

        longest_dia = max(root_diameter, left_diameter, right_diameter)
        longest_edge = max(left_longest_edge, right_longest_edge)

        return longest_edge, longest_dia


        