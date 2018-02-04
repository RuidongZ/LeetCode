# -*- Encoding:UTF-8 -*-

# 415. Add Strings

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = ""
        num1 = num1[::-1]
        num2 = num2[::-1]
        n1 = len(num1)
        n2 = len(num2)

        tmp = "0"*abs(n2-n1)
        if n1 > n2:
            num2 += tmp
        elif n2 > n1:
            num1 += tmp

        length = max(n1, n2)

        tmp = 0
        for i in range(length):
            a = ord(num1[i]) - ord('0')
            b = ord(num2[i]) - ord('0')
            c = a + b + tmp
            tmp = 0
            if c >= 10:
                c -= 10
                tmp = 1
            ans += chr(ord('0') + c)

        if tmp > 0:
            ans += "1"

        return ans[::-1]
