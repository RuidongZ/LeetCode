# -*- Encoding:UTF-8 -*-

# 66. Plus One

# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.insert(0, 0)

        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                break
            else:
                digits[i] -= 10

        if digits[0] == 0:
            digits.pop(0)

        return digits
