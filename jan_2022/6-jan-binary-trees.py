from misc.TreeNode import Node


# Question 1:
"""
Binary tree - same
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

"""

## search O(log(n))
# [1, 2, 3, 6, 8, 10, 11, 21]

#
#         1    |    1
#       2   3  |  3   2
#     4  5 6 7 | 7 6 5 4
#


# class Node:
#     def __init__(self, val):
#         self.left = None
#         self.right = None
#         self.val = val


def sameTree(p: Node, q: Node):
    # p or q is None ==> None.val Error
    if p is None and q is None:
        return True

    if p is None and q is not None:
        return False

    if p is not None and q is None:
        return False

    if p.val == q.val:
        return sameTree(p.left, q.right) and sameTree(p.right, q.left)

    return False


# Question 2
"""
Binary tree - Symmetric trees
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""


def isSymmetric(head: Node):

    return sameTree(head.left, head.right)


## Data and test cases
root1 = Node(2)
root1.left = Node(1)
root1.left.left = None
root1.left.right = Node(4)
root1.right = Node(3)
root1.right.left = Node(7)
root1.right.right = Node(6)

root2 = Node(2)
root2.insert(1)
root2.insert(3)
root2.insert(4)
root2.insert(12)

root2_invert = Node(2)
root2_invert.left = Node(3)
root2_invert.right = Node(1)

root3 = Node(4)
root3.insert(1)
root3.insert(5)
root3.insert(2)
root3.insert(8)

# print(sameTree(root1, root1))  # true
# print(sameTree(root2, root2_invert))  # false
# print(sameTree(root1, root3))  # false

symHead = Node(1)
symHead.left = Node(2)
symHead.left.left = Node(3)
symHead.left.right = Node(4)

symHead.right = Node(2)
symHead.right.left = Node(4)
symHead.right.right = Node(3)
print(isSymmetric(symHead))  # True
