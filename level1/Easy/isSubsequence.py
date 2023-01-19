#O(n) time | O(1) space
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #base case
        if len(s) > len(t):
            return False
        #have 2 pointers at the beginning of each string
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
                
