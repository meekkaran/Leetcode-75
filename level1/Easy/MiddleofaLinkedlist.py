#O(n) time | O(1) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #when fast pointer is at the end , the slow is at midpoint
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
            
           
            
