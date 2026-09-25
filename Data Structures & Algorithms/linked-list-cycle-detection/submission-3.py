# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #if head.next is None:
        #    return False

        seenNodes = set()

        curr = head
        
        while curr is not None:
            if curr in seenNodes:
                return True
            seenNodes.add(curr)
            curr = curr.next

        return False