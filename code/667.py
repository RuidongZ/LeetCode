# -*- Encoding:UTF-8 -*-

# 667. Beautiful Arrangement II

# Given two integers n and k, you need to construct a list which contains n different positive integers
# ranging from 1 to n and obeys the following requirement:
# Suppose this list is [a1, a2, a3, ... , an],
# then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
#
# If there are multiple answers, print any of them.
#
# Example 1:
# Input: n = 3, k = 1
# Output: [1, 2, 3]
# Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3,
# and the [1, 1] has exactly 1 distinct integer: 1.
# Example 2:
# Input: n = 3, k = 2
# Output: [1, 3, 2]
# Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3,
# and the [2, 1] has exactly 2 distinct integers: 1 and 2.
# Note:
# The n and k are in the range 1 <= k < n <= 104.


class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        '''Better Solution'''
        '''
        ans = range(1, n-k)
        for i in range(k+1):
            if i % 2 == 0:
                ans.append(n-k + i/2)
            else:
                ans.append(n - i/2)
        return ans
        '''
        ans = []
        left = 1
        right = n
        while k >= 1:
            if k % 2 != 0:
                ans.append(left)
                left += 1
            else:
                ans.append(right)
                right -= 1
            k -= 1
        for i in range(left, right+1):
            ans.append(i)
        return ans
