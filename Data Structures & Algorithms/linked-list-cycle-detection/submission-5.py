# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        l,r = head,head.next # two indexes

        index = -1
        while l is not None and (r and r.next) is not None:
            if l == r:
                return True
            l = l.next
            r = r.next.next
        return False