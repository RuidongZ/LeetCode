# -*- Encoding:UTF-8 -*-

# 9. Palindrome Number

# Determine whether an integer is a palindrome. Do this without extra space.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        a = x
        b = 0

        while a > 0:
            tmp = a % 10
            b *= 10
            b += tmp
            a //= 10

        return b == x
