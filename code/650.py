# -*- Encoding:UTF-8 -*-

# 650. 2 Keys Keyboard

# Initially on a notepad only one character 'A' is present.
# You can perform two operations on this notepad for each step:

# Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted.
# Output the minimum number of steps to get n 'A'.
#
# Example 1:
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
# Note:
# The n will be in the range [1, 1000].


class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        if n == 1:
            return ans
        while True:
            tmp = self.getMaxFactor(n)
            if not tmp:
                ans += n
                break
            ans += n // tmp
            n = tmp
        return ans

    def getMaxFactor(self, n):
        import math
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return n // i
        return None
