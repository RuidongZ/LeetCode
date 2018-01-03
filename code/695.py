# -*- Encoding:UTF-8 -*-

# 695. Max Area of Island

# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.

class Solution(object):
    tmpgrid = None
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.tmpgrid = grid
        ans = 0
        tmp = 0
        for i in range(len(self.tmpgrid)):
            for j in range(len(self.tmpgrid[i])):
                if self.tmpgrid[i][j] == 1:
                    tmp += self.dfs(self.tmpgrid, i, j)
                    ans = max(ans, tmp)
                    tmp = 0
        return ans


    def dfs(self, grid, i, j):
        ans = 1
        grid[i][j] = 0
        if i+1 < len(grid) and grid[i+1][j] == 1:
            ans += self.dfs(grid, i+1, j)
        if j+1 < len(grid[0]) and grid[i][j+1] == 1:
            ans += self.dfs(grid, i, j+1)
        if i-1 > -1 and grid[i-1][j] == 1:
            ans += self.dfs(grid, i-1, j)
        if j-1 > -1 and grid[i][j-1] == 1:
            ans += self.dfs(grid, i, j-1)
        return ans
