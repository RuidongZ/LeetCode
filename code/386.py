# -*- Encoding:UTF-8 -*-

# 386. Lexicographical Numbers

# Given an integer n, return 1 - n in lexicographical order.
#
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
#
# Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        self.ans = []
        self.dfs(1, n)
        return self.ans

    def dfs(self, n, max):
        if n > max:
            return
        i = 0
        while n % 10 + i <= 9:
            if n+i <= max:
                self.ans.append(n+i)
                self.dfs((n+i)*10, max)
            else:
                break
            i += 1
        return

