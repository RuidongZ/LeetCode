# -*- Encoding:UTF-8 -*-

# 22. Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:
#
# [
#     "((()))",
#     "(()())",
#     "(())()",
#     "()(())",
#     "()()()"
# ]


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        tmp = ""
        self.dfs(ans, tmp, n, n)
        return ans

    def dfs(self, ans, current, left, right):
        if left > right:
            return
        if left == 0 and right == 0:
            ans.append(current)
            return
        if left > 0:
            self.dfs(ans, current+"(", left-1, right)
        if right > 0:
            self.dfs(ans, current+")", left, right-1)
