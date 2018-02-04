# -*- Encoding:UTF-8 -*-

# 202. Happy Number

# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp = set()
        while True:
            if n == 1:
                return True
            if n in tmp:
                return False
            tmp.add(n)
            n = self.replace(n)

    def replace(self, n):
        ans = 0
        s = str(n)
        for i in s:
            ans += int(i)**2
        return ans
