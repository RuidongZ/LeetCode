# -*- Encoding:UTF-8 -*-

# 583. Delete Operation for Two Strings

# Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same,
# where in each step you can delete one character in either string.
#
# Example 1:
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
# Note:
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1) + 1
        n = len(word2) + 1
        dp = [([0]*m) for _ in range(n)]
        # Find num of Common chars
        for i in range(1, n):
            for j in range(1, m):
                if word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return len(word1)+len(word2)-2*dp[-1][-1]
