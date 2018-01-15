# -*- Encoding:UTF-8 -*-

# 762. Prime Number of Set Bits in Binary Representation

# Given two integers L and R, find the count of numbers in the range [L, R] (inclusive)
# having a prime number of set bits in their binary representation.

# (Recall that the number of set bits an integer has is the number of 1s present when written in binary.
# For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)
#
# Example 1:
#
# Input: L = 6, R = 10
# Output: 4
# Explanation:
# 6 -> 110 (2 set bits, 2 is prime)
# 7 -> 111 (3 set bits, 3 is prime)
# 9 -> 1001 (2 set bits , 2 is prime)
# 10->1010 (2 set bits , 2 is prime)
# Example 2:
#
# Input: L = 10, R = 15
# Output: 5
# Explanation:
# 10 -> 1010 (2 set bits, 2 is prime)
# 11 -> 1011 (3 set bits, 3 is prime)
# 12 -> 1100 (2 set bits, 2 is prime)
# 13 -> 1101 (3 set bits, 3 is prime)
# 14 -> 1110 (3 set bits, 3 is prime)
# 15 -> 1111 (4 set bits, 4 is not prime)

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        ans = 0
        d = {}
        for i in range(L, R+1):
            bits = self.countbits(i)
            if bits not in d:
                tmp = self.isPrime(bits)
                d[bits] = tmp
            else:
                tmp = d[bits]
            if tmp:
                ans += 1
        return ans

    def countbits(self, n):
        return bin(n).count("1")

    def isPrime(self, n):
        if n <= 1:
            return False
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
