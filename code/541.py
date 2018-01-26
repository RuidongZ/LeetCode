# -*- Encoding:UTF-8 -*-

# 541. Reverse String II

# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting
# from the start of the string. If there are less than k characters left, reverse all of them.
# If there are less than 2k but greater than or equal to k characters,
# then reverse the first k characters and left the other as original.

# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = ""
        start = 0
        revese = True
        while True:
            if start >= len(s):
                break
            end = min(start+k, len(s))

            if revese:
                tmp = s[start:end][::-1]
                ans += tmp
                revese = False
            else:
                tmp = s[start:end]
                ans += tmp
                revese = True
            start = end
        return ans
