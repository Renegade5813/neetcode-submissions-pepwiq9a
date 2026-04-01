# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        left = head

        def getLast(curr):
            prev = []
            while curr.next:
                prev.append(curr)
                curr = curr.next
            return curr, prev

        right, prevStack = getLast(left)

        while left != right and left.next != right:
            temp = left.next
            left.next = right
            right.next = temp

            left = temp
            right = prevStack.pop()

        right.next = None
