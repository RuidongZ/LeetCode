# -*- Encoding:UTF-8 -*-

# 52. N-Queens II

# Follow up for N-Queens problem.

# Now, instead outputting board configurations, return the total number of distinct solutions.


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = [([0]*n) for _ in range(n)]
        i = 0
        return self.dfs(m, i)

    def dfs(self, m, i):
        ans = 0
        if i == len(m):
            return 1
        for j in range(len(m[0])):
            if m[i][j] == 0:
                import copy
                tmp = copy.deepcopy(m)
                self.change(tmp, i, j)
                ans += self.dfs(tmp, i+1)
        return ans

    def change(self, m, i, j):
        for r in range(len(m)):
            for c in range(len(m[0])):
                if r == i or c == j:
                    m[r][c] = 1
                if abs(r-i) == abs(c-j):
                    m[r][c] = 1

