class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ""
        #use min and max to sort and retrieve in alphabetical order
        str1 = min(strs)
        str2 = max(strs)
        for i , c in enumerate(str1):
            if c != str2[i]:
                return str1[:i]

           return str1
    
###solution 2
## O(n(log(n)) time and O(n) space
        ans = ""
        v = sorted(strs)
        v1 = v[0]
        v2 = v[-1]
        for i in range(min(len(v1),len(v2))):
            if v1[i] != v2[i]
                return ans
            ans += v1[i]
        return ans
