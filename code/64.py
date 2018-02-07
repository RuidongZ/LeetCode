# -*- Encoding:UTF-8 -*-

# 64. Minimum Path Sum

# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example 1:
# [[1,3,1],
#  [1,5,1],
#  [4,2,1]]
# Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [([0] * n) for _ in range(m)]

        tmp = 0
        for i in range(n):
            tmp += grid[0][i]
            dp[0][i] = tmp

        tmp = 0
        for i in range(m):
            tmp += grid[i][0]
            dp[i][0] = tmp

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]
