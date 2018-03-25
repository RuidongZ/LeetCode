# -*- Encoding:UTF-8 -*-

# 507. Perfect Number

# We define the Perfect Number is a positive integer
# that is equal to the sum of all its positive divisors except itself.
#
# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# Note: The input number n will not exceed 100,000,000. (1e8)


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 6:
            return False

        import math
        total = 1
        end = int(math.sqrt(num))

        for i in range(2, end+1):
            if num % i == 0:
                total += i
                total += num//i
        return total == num
