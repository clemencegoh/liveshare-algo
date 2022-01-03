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


def generate_from_array(arr, lastPtr=-1):
    if len(arr) == 0:
        return None

    head = SingleListNode(arr[0], None)
    prev = head

    for i in range(1, len(arr)):
        prev.next = SingleListNode(arr[i], None)
        prev = prev.next

    if lastPtr != -1:
        curr = lastPtr
        pointingTo = head
        while curr > 0:
            pointingTo = pointingTo.next
            curr -= 1
        prev.next = pointingTo
    return head
