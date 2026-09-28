# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        second = s.next
        s.next = None

        # reverse second half
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1,temp2