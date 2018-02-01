# -*- Encoding:UTF-8 -*-

# 516. Longest Palindromic Subsequence

# Given a string s, find the longest palindromic subsequence's length in s.
# You may assume that the maximum length of s is 1000.
#
# Example 1:
# Input: "bbbab"
# Output: 4
# One possible longest palindromic subsequence is "bbbb".

# Example 2:
# Input: "cbbd"
# Output: 2
# One possible longest palindromic subsequence is "bb".


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dp = [([0] * length) for _ in range(length)]

        for i in range(length-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
