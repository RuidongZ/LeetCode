# -*- Encoding:UTF-8 -*-

# 12. Integer to Roman

# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        strs = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"],
                [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"],
                [5, "V"], [4, "IV"], [1, "I"]]
        ans = ""
        i = 0
        while num > 0:
            j = 0
            k = num // strs[i][0]
            while j < k:
                ans += strs[i][1]
                j += 1
            num %= strs[i][0]
            i += 1
        return ans
