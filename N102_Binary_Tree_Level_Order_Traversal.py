# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = [(0, root)]
        while queue:
            level, node = queue.pop(0)
            if level >= len(result):
                result.append([])
            result[level].append(node.val)

            next_level = level + 1
            if node.left:
                queue.append((next_level, node.left))
            if node.right:
                queue.append((next_level, node.right))
        return result


# DFS
class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        traversals = []
        self.dfs(root, 0, traversals)
        return traversals

    def dfs(self, root, level, traversals):
        if level >= len(traversals):
            traversals.append()
        traversals[level].append(root.val)
        if root.left:
            self.dfs(root.left, level+1, traversals)
        if root.right:
            self.dfs(root.left, level+1, traversals)
