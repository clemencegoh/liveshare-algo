# List of easy algorithms that I find interesting

https://leetcode.com/problems/range-sum-of-bst/

https://leetcode.com/problems/two-sum/

https://leetcode.com/problems/merge-two-sorted-lists/

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Reverse Singly Linked List in place (recursion)

## Binary tree - same

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

![true example](./resources/binTreeTrue.jpg)

```python

# data
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

def sameTree(p, q):
    pass

print(sameTree(root1, root2)) # true
print(sameTree(root2, root2_invert)) # false
print(sameTree(root1, root3))  # false

```

## Binary tree - Symmetric trees

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
![symmetric tree true example](./resources/symtree1.jpg)

```python

# data
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

def symmetricTree(p, q):
    pass

print(symmetricTree(root1, root2)) # false
print(symmetricTree(root2, root2_invert)) # true
print(symmetricTree(root1, root3))  # false

```
