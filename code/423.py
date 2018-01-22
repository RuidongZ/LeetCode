# -*- Encoding:UTF-8 -*-

# 423. Reconstruct Original Digits from English

# Given a non-empty string containing an out-of-order English representation of digits 0-9,
# output the digits in ascending order.

# Note:
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original digits.
# That means invalid inputs such as "abc" or "zerone" are not permitted.
# Input length is less than 50,000.
# Example 1:
# Input: "owoztneoer"
#
# Output: "012"
# Example 2:
# Input: "fviefuro"
# Output: "45"


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        z0 = s.count("z")
        w2 = s.count("w")
        u4 = s.count("u")
        x6 = s.count("x")
        g8 = s.count("g")

        s7 = s.count("s") - x6
        v5 = s.count("v") - s7
        i9 = s.count("i") - v5 - x6 - g8
        h3 = s.count("h") - g8
        o1 = s.count("o") - z0 - w2 - u4

        ans += "0" * z0
        ans += "1" * o1
        ans += "2" * w2
        ans += "3" * h3
        ans += "4" * u4
        ans += "5" * v5
        ans += "6" * x6
        ans += "7" * s7
        ans += "8" * g8
        ans += "9" * i9
        return ans
