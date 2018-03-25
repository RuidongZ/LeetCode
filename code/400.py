# -*- Encoding:UTF-8 -*-

# 400. Nth Digit

# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
#
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).
#
# Example 1:
#
# Input:
# 3
#
# Output:
# 3

# Example 2:
#
# Input:
# 11
#
# Output:
# 0
#
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        k = 1
        while n > total:
            total += 9*k*(10**(k-1))
            k += 1

        k -= 1
        total -= 9*k*(10**(k-1))

        counts = (n - total)//k
        idx = (n-total) % k

        target = 10**(k-1) + counts - 1

        return target % 10 if idx == 0 else int(str(target+1)[idx-1])

