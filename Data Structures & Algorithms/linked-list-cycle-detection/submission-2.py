# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #if head.next is None:
        #    return False

        seenNodes = {}

        curr = head
        index = 0
        while curr is not None:
            if curr in seenNodes:
                return True
            seenNodes[curr] = index
            curr = curr.next
            index += 1

        return False