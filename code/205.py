# -*- Encoding:UTF-8 -*-

# 205. Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}

        length = len(s)

        i = 0
        while i < length:
            if s[i] not in d1 and t[i] not in d2:
                d1[s[i]] = i
                d2[t[i]] = i
            elif s[i] in d1 and t[i] in d2:
                if d1[s[i]] != d2[t[i]]:
                    return False
            else:
                return False
            i += 1
        return True
