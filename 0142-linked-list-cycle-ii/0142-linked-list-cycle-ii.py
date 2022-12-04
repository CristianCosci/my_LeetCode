# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        while fast and fast.next and fast.next.next:
            if fast.next.next == slow.next:
                slow = slow.next
                while True:
                    if head == slow:
                        return slow
                    else:
                        head = head.next
                        slow = slow.next
            else:
                fast = fast.next.next
                slow = slow.next
        
        return None
        