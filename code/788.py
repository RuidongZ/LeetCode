# -*- Encoding:UTF-8 -*-

# 788. Rotated Digits

# X is a good number if after rotating each digit individually by 180 degrees, we get a valid number
# that is different from X. A number is valid if each digit remains a digit after rotation. 0, 1,
# and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other,
# and the rest of the numbers do not rotate to any other number.
#
# Now given a positive number N, how many numbers X from 1 to N are good?
#
# Example:
# Input: 10
# Output: 4
# Explanation:
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# Note:
# N  will be in range [1, 10000].


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        cnt = 0
        for i in range(1, N+1):
            if self.isValid(i):
                cnt += 1
        return cnt

    def isValid(self, n):
        ans = False
        while n > 0:
            if n % 10 == 2:
                ans = True
            if n % 10 == 5:
                ans = True
            if n % 10 == 6:
                ans = True
            if n % 10 == 9:
                ans = True
            if n % 10 == 3:
                return False
            if n % 10 == 4:
                return False
            if n % 10 == 7:
                return False
            n = n // 10
        return ans
