# -*- Encoding:UTF-8 -*-

# 343. Integer Break

# Given a positive integer n, break it into the sum of at least two positive integers and
# maximize the product of those integers. Return the maximum product you can get.
#
# For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
#
# Note: You may assume that n is not less than 2 and not larger than 58.
#
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(2, n+1):
            tmp = n
            prod = 1
            l = tmp // i
            while tmp != 0:
                if tmp % i != 0:
                    prod *= l+1
                    tmp -= l+1
                    i -= 1
                else:
                    for _ in range(i):
                        prod *= l
                    break
            if prod > ans:
                ans = prod
            else:
                break
        return ans
