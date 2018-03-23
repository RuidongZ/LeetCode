# -*- Encoding:UTF-8 -*-

# 20. Valid Parentheses

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ('(', '[', '{')
        right = (')', ']', '}')

        tmp = []

        for i in s:
            if i in left:
                tmp.append(i)
            else:
                if tmp:
                    if right.index(i) != left.index(tmp.pop()):
                        return False
                else:
                    return False

        return not tmp
