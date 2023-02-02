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
