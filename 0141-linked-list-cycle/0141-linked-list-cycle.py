# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        else:
            while True:
                if head.next == None:
                    return False
                elif head.val == '':
                    return True
                else:
                    head.val = ''
                    head = head.next
                    
            return cycle