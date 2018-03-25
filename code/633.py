# -*- Encoding:UTF-8 -*-

# 633. Sum of Square Numbers

# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.
#
# Example 1:
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:
# Input: 3
# Output: False


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # Better Way
        # Fermat's Theorem:
        # "Any positive number n is expressible as a sum of two squares
        # if and only if the prime factorization of n, every prime of the form (4k+3) occurs an even number of times."
        '''
        i = 2
        while i**2 <= c:
            count = 0
            if c % i == 0:
                while c % i == 0:
                    count += 1
                    c /= i
                if i % 4 == 3 and count % 2 != 0:
                    return False
            i += 1
        return c % 4 != 3
        '''
        for i in range(int(c**0.5)+1):
            j = c - i**2
            if int(j**0.5)**2 == j:
                return True
        return False
