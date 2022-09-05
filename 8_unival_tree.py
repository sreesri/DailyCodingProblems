"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""
"""
Notes:
    If all the nodes of a tree has same value then the tree is called a unival tree. The leaf nodes can be counted as one unival tree.
"""


class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.right = right
        self.left = left


def is_unival_tree(root):
    return unival_checker(root, root.value)


def unival_checker(root, root_val):
    if root is None:
        return True
    if root.value == root_val:
        return unival_checker(root.left, root_val) and unival_checker(root.right, root_val)
    return False


def count_unival_subtrees(root):
    if root is None:
        return 0
    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)
    return 1 + left + right if is_unival_tree(root) else left + right


if __name__ == "__main__":
    root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    print(count_unival_subtrees(root))

    root = Node('a', Node('a'), Node('a', Node('a'), Node('a',None, Node('A'))))
    print(count_unival_subtrees(root))

    root = Node('a', Node('c'), Node('b', Node('b'), Node('b', None, Node('b'))))
    print(count_unival_subtrees(root))
