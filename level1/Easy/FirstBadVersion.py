# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
#O(log(n)) time due to bnary search and O(1)space
class Solution:
    def firstBadVersion(self, n: int) -> int:
        #create 2 pointers
        l = 1
        r = n 
        while l <= r:
            mid = (l+r)//2
            if isBadVersion(mid) == False:
                l = mid + 1
            else:
                r = mid - 1
        return l
        
