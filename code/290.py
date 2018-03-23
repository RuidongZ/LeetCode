# -*- Encoding:UTF-8 -*-

# 290. Word Pattern

# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection
# between a letter in pattern and a non-empty word in str.
#
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters,
# and str contains lowercase letters separated by a single space.


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        plen = len(pattern)
        str = str.split(" ")
        slen = len(str)

        if plen != slen:
            return False
        d1 = {}
        d2 = {}
        for i in range(plen):
            if pattern[i] in d1 and str[i] in d2:
                if str[i] != d1[pattern[i]] or pattern[i] != d2[str[i]]:
                    return False
            elif pattern[i] not in d1 and str[i] not in d2:
                d1[pattern[i]] = str[i]
                d2[str[i]] = pattern[i]
            else:
                return False
        return True
