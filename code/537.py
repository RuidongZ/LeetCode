# -*- Encoding:UTF-8 -*-

# 537. Complex Number Multiplication
# Given two strings representing two complex numbers.
# You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

# Example 1:
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

# Note:
# The input strings will not have extra blank.
# The input strings will be given in the form of a+bi,
# where the integer a and b will both belong to the range of [-100, 100].
# And the output should be also in this form.


class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a.split("+")
        b = b.split("+")

        x1 = int(a[0])
        x2 = int(a[1][:-1])

        y1 = int(b[0])
        y2 = int(b[1][:-1])

        x = x1*y1 - x2*y2
        y = x1*y2 + x2*y1

        return str(x)+"+"+str(y)+"i"
