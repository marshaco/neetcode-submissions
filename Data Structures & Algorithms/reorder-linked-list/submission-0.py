# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find length of the list
        length = 0
        tail = head
        while tail is not None:
            length += 1
            tail = tail.next

        middle = length - (length // 2)

        prevMiddle = None
        middleNode = head
        while middle > 0:
            prevMiddle = middleNode
            middleNode = middleNode.next
            middle -= 1
        prevMiddle.next = None
        

        # Reverse the middle
        prev = None
        while middleNode is not None:
            nextNode = middleNode.next
            middleNode.next = prev

            prev = middleNode
            middleNode = nextNode

        # Merge two lists
        curr = head
        while prev is not None:
            nextNode = curr.next
            mNextNode = prev.next

            curr.next = prev
            prev.next = nextNode

            curr = nextNode
            prev = mNextNode

        return