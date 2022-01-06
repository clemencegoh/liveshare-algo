## Workspace for sessions and algo solving drafts - Vernon
from misc.TreeNode import Node


def sameTree(p: Node, q: Node):
    pass


## Data and test cases
root1 = Node(2)
root1.insert(1)
root1.insert(3)

root2 = Node(2)
root2.insert(1)
root2.insert(3)

root2_invert = Node(2)
root2_invert.left = Node(3)
root2_invert.right = Node(1)

root3 = Node(4)
root3.insert(1)
root3.insert(5)
root3.insert(2)
root3.insert(8)

print(sameTree(root1, root2))  # true
print(sameTree(root2, root2_invert))  # false
print(sameTree(root1, root3))  # false
