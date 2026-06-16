# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        while len(lists)>1:
            mergedList =[]
            for i in range(0,len(lists),2):
                list1= lists[i]
                list2 = lists[i+1] if (i+1)< len(lists) else None
                mergedList.append(self.merge(list1,list2))
            lists=mergedList
        return lists[0]
    
    def merge(self, a, b):
        dummy= ListNode()
        current=dummy
        while a and b:
            if a.val < b.val:
                current.next= a
                a=a.next
            else:
                current.next=b
                b=b.next
            current=current.next
        if a:
            current.next=a
        if b:
            current.next=b
        return dummy.next
        