# -*- Encoding:UTF-8 -*-

# 357. Count Numbers with Unique Digits

# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

# Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100,
# excluding [11,22,33,44,55,66,77,88,99])


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 1
        for i in range(n):
            val = 9
            tmp_ans = 9
            for j in range(i):
                tmp_ans *= val
                val -= 1
            ans += tmp_ans
        return ans
