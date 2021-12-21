# Definition for singly-linked list.
class SingleListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def generate_sorted_linked_list(mini, maxi, start):
    head = SingleListNode(start, None)
    prev = head
    for i in range(mini, maxi):
        prev.next = SingleListNode(i, None)
        prev = prev.next
    return head
