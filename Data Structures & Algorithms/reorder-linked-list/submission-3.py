# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f=head, head
        while f and f.next:
            s=s.next
            f=f.next.next
        prev,curr=None, s.next
        s.next=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        l1,l2=head,prev
        while l2:
            temp1,temp2=l1.next,l2.next
            l1.next=l2
            l2.next=temp1
            l1,l2=temp1,temp2