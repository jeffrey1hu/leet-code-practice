# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# search a value in a bst
def find(root, k):
    if not root:
        return None

    if root.val == k:
        return root.val
    elif root.val > k:
        return find(root.right, k)
    else:
        return find(root.left, k)

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        if root.val > node.val:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
    return root


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            if root.right is None:
                temp = root.left
                return temp

            temp = self._find_min_val_node(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        return root

    def _find_min_val_node(self, root):
        """
        :param root: The root of a BST
        :return: node with min val in the tree
        """
        if root is None:
            return None

        if not root.left:
            return root
        else:
            return self._find_min_val_node(root.left)



def min_value(root):
    if root is None:
        return None

    if root.left:
        return min_value(root.left)
    else:
        return root.val


def max_value(root):
    if root is None:
        return None

    if root.right:
        return max_value(root.right)
    else:
        return root.val


def check_is_bst(root):
    # An empty tree is bst
    if root is None:
        return True
    if root.right is None and root.left is None:
        return True

    if root.left:
        max_left_subtree = max_value(root.left)
    else:
        max_left_subtree = root.val

    if root.right:
        min_right_subtree = min_value(root.right)
    else:
        min_right_subtree = root.val

    if min_right_subtree > max_left_subtree:
        return True

    return check_is_bst(root.left) and check_is_bst(root.right)

# inorder traverse
def check_is_bst_impr(root):
    return _check_is_bst_utils(root, min_val=-float('inf'), max_val=float('inf'))

def _check_is_bst_utils(root, min_val, max_val):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.val > min_val and root.val < max_val:
        return _check_is_bst_utils(root.left, min_val, root.val) and _check_is_bst_utils(root.right, root.val, max_val)
    else:
        return False

# print keys in given range
def print_bst_keys_in_give_range(root, k1, k2):
    if not root:
        return
    if root.val >= k1 and root.val <= k2:
        print root.val
    if root.val < k2:
        print_bst_keys_in_give_range(root.left, k1, k2)
    if root.val > k1:
        print_bst_keys_in_give_range(root.right, k1, k2)

# merge two bst to get a sorted array
def merge_two_bst(root1, root2):
    if root1 is None and root2 is None:
        return []
    if root1 is None:
        return list(generate_inorder_traverse_of_bst(root2))
    if root2 is None:
        return list(generate_inorder_traverse_of_bst(root1))

    stack1 = []
    stack2 = []
    result = []
    gen1 = generate_inorder_traverse_of_bst(root1)
    gen2 = generate_inorder_traverse_of_bst(root2)

    while True:
        try:
            if not stack1:
                stack1.append(gen1.next())
            if not stack2:
                stack2.append(gen2.next())
        except StopIteration:
            result.extend(stack1)
            result.extend(list(gen1))
            result.extend(stack2)
            result.extend(list(gen2))
            break
        if stack1[0] < stack2[0]:
            result.append(stack1.pop())
        else:
            result.append(stack2.pop())
    return result


def generate_inorder_traverse_of_bst(root):
    if root.left:
        generate_inorder_traverse_of_bst(root.left)
    yield root.val
    if root.right:
        generate_inorder_traverse_of_bst(root.right)


if __name__ == '__main__':
    node = TreeNode(4)
    root = None
    root = insert(root, node)
    print root