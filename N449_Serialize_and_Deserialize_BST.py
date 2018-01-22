# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        nodes_pre_order = []
        self.pre_order_traverse(root, nodes_pre_order)
        return ','.join(nodes_pre_order)

    def pre_order_traverse(self, root, result):
        if root is None:
            return
        result.append(str(root.val))
        if root.left:
            self.pre_order_traverse(root.left, result)
        if root.right:
            self.pre_order_traverse(root.right, result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        pre_list = []

        def deserialize_util(nodes, pre_list, min_val, max_val):
            if not nodes:
                return None

            if len(pre_list) >= len(nodes):
                return None

            if nodes[len(pre_list)] < min_val or nodes[len(pre_list)] > max_val:
                return None

            root = TreeNode(nodes[len(pre_list)])
            pre_list.append(nodes[len(pre_list)])

            root.left = deserialize_util(nodes, pre_list, min_val, root.val)
            root.right = deserialize_util(nodes, pre_list, root.val, max_val)

            return root

        nodes_pre_order = map(int, filter(lambda x: x, data.split(',')))
        return deserialize_util(nodes_pre_order, pre_list, -float('inf'), float('inf'))





# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))