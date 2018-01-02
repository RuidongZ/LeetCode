# -*- Encoding:UTF-8 -*-

# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        ans = ""
        length = len(min(strs))
        for i in range(length):
            for s in strs[1:]:
                if s[i] != strs[0][i]:
                    return ans
            ans.join(strs[0][i])
        return ans

    '''
    # bettter one
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if strs is not None and len(strs) > 0:
            strs.sort()
            a = strs[0]
            b = strs[len(strs) - 1]

            for i in range(len(a)):
                if len(b) > i and a[i] == b[i]:
                    res += b[i]
                else:
                    return res
        return res
    '''