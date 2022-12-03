# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        while head.next:
            middle = middle.next
            if head.next.next:
                head = head.next.next
            else:
                break
        
        return middle
        