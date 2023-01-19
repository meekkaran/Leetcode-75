#O(n) time and O(1) space
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #Create two maps for s & t strings...
        #Traverse all elements through the loop...
        #Compare the maps, if not equal, return false...
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        return map1 == map2
