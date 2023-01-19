# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #O(n) time |  O(1)space
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #create three pointers
        p1 = None
        p2 = head
        while p2 is not None:
            p3 = p2.next #another pointer p3
            p2.next = p1
            p1 = p2
            p2 = p3
        return p1

        
