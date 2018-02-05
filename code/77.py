# -*- Encoding:UTF-8 -*-

# 77. Combinations

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# For example,
# If n = 4 and k = 2, a solution is:
#
# [
#     [2,4],
#     [3,4],
#     [2,3],
#     [1,2],
#     [1,3],
#     [1,4],
# ]


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        ans = []
        self.dfs(ans, [], n, 1, k)
        return ans

    def dfs(self, ans, tmp, n, cur, left):
        if left == 0:
            ans.append(list(tmp))
            return

        for i in range(cur, n-left+1):
            tmp.append(i)
            self.dfs(ans, tmp, n, i+1, left-1)
            tmp.pop()
