# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS method inorder of node

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node_vals = []
        self.in_order_nodes_iter(node_vals, root)

        min_dist = float('inf')
        for i in range(1, len(node_vals)):
            temp_dist = node_vals[i] - node_vals[i-1]
            if temp_dist < min_dist:
                min_dist = temp_dist
        return min_dist

    def in_order_nodes_iter(self, node_vals, root):

        if root.left:
            self.in_order_nodes_iter(node_vals, root.left)
        node_vals.append(root.val)
        if root.right:
            self.in_order_nodes_iter(node_vals, root.right)
