# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast, prev = head, head, None
        #find midpoint using floyd's
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        #reversal
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        #comparison
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True

        
