# -*- Encoding:UTF-8 -*-

# 712. Minimum ASCII Delete Sum for Two Strings

# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.
# Example 1:
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
#
# Example 2:
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
#
# Note:
# 0 < s1.length, s2.length <= 1000.
# All elements of each string will have an ASCII value in [97, 122].


class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        # m = [[0] * (len(s1)+1)]*(len(s2)+1) Bad Initial
        m = [([0] * (len(s1)+1)) for i in range(len(s2)+1)]
        for i in range(1, len(m[0])):
            m[0][i] = ord(s1[i-1]) + m[0][i-1]
        for i in range(1, len(m)):
            m[i][0] = ord(s2[i-1]) + m[i-1][0]
        for i in range(1, len(m)):
            for j in range(1, len(m[0])):
                if s1[j-1] == s2[i-1]:
                    m[i][j] = m[i-1][j-1]
                else:
                    a = m[i-1][j]+ord(s2[i-1])
                    b = m[i][j-1]+ord(s1[j-1])
                    m[i][j] = min(a, b)
        return m[-1][-1]
