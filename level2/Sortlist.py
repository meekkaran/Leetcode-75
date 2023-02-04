# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #midpoint -helper
    def getMid(self,head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    #merge -helper
    def merge(self,list1,list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
            
        return dummy.next
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
     #three steps
    #1. find midpoint
    #2:perform mergesort
    #3.sort
        if not head or not head.next:
            return head
    
        left = head
        mid = self.getMid(head)
        right = mid.next
        mid.next = None


        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)
    
            


            
