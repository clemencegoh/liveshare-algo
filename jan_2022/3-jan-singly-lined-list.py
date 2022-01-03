"""
Given the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

---
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

---
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""


from misc.singlyLinkedListNode import SingleListNode, generate_from_array

"""

# Definition for singly-linked list.
class SingleListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.isBeingRead = False

[1,2] 
x = SingleListNode(val = 1)
y = SingleListNode(val = 2)
x.next = y
x.val == 1
x.next.val == 2

while x is not None:
    print(x.val)
    x = x.next

head.next.val == x.next.val


[1, 2, 2, 4, 6]
[ ,  , ^,  ,  ]  => ptr 1
[ ,  , ^,  ,  ]  => ptr 2

"""

# Time complexity O(n)
# Space complexity O(n)
def cycleInList(head: SingleListNode):
    x = head
    repeat = True
    dictionary = set()

    while repeat:
        if x.next is None:
            return False

        elif x.val in dictionary:
            return True

        else:
            dictionary.add(x.val)
            x = x.next


firstList = generate_from_array([3, 2, 0, -4, 8, 7], 2)
secondList = generate_from_array([1, 2], 0)
thirdList = generate_from_array([1])
fourthList = generate_from_array([1, 4, 5, 8, 3, 2])

print(cycleInList(firstList))
print(cycleInList(secondList))
print(cycleInList(thirdList))
print(cycleInList(fourthList))

# verification
# head = firstList
# listcount = []
# for i in range(20):
#     listcount.append(head.val)
#     head = head.next
# print(listcount)


assert cycleInList(firstList) == True
assert cycleInList(secondList) == True
assert cycleInList(thirdList) == False
assert cycleInList(fourthList) == False
print("complete")
