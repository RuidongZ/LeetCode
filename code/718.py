# -*- Encoding:UTF-8 -*-

# 718. Maximum Length of Repeated Subarray

# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
#
# Example 1:
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation:
# The repeated subarray with maximum length is [3, 2, 1].
# Note:
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A) + 1
        m = len(B) + 1
        dp = [([0] * n) for _ in range(m)]
        ans = 0
        for i in range(1, m):
            for j in range(1, n):
                if A[j-1] == B[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ans = max(ans, dp[i][j])
        return ans
