# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next==None:
            return head
        cur=head
        prev=head
        while (cur.next):
            new_cur=cur.next
            if cur==head:
                cur.next=None
            else:
                cur.next= prev
            prev=cur
            cur=new_cur
        
        cur.next=prev
        head=cur
 
                
        
        return head

        