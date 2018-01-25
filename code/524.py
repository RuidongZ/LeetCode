# -*- Encoding:UTF-8 -*-

# 524. Longest Word in Dictionary through Deleting

# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by
# deleting some characters of the given string. If there are more than one possible results, return the longest word
# with the smallest lexicographical order. If there is no possible result, return the empty string.
#
# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# Output:
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]
#
# Output:
# "a"
# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        s = list(s)
        d = sorted(d, key=lambda x: (-len(x), x))
        for i in d:
            if self.isInString(s, i):
                return i
        return ""

    def isInString(self, s, w):
        cur = 0
        for i in w:
            if i in s[cur:]:
                cur = cur + s[cur:].index(i) + 1
            else:
                return False
        return True
