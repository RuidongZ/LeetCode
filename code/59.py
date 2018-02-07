# -*- Encoding:UTF-8 -*-

# 59. Spiral Matrix II

# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# For example,
# Given n = 3,
#
# You should return the following matrix:
# [
#     [ 1, 2, 3 ],
#     [ 8, 9, 4 ],
#     [ 7, 6, 5 ]
# ]


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [([0] * n) for _ in range(n)]
        import math
        tmp = 1
        for i in range(math.ceil(n/2)):
            for j in range(i, n-i):
                matrix[i][j] = tmp
                tmp += 1

            for j in range(i+1, n-i):
                matrix[j][n-1-i] = tmp
                tmp += 1

            for j in range(n-i-2, i-1, -1):
                matrix[n-i-1][j] = tmp
                tmp += 1

            for j in range(n-i-2, i, -1):
                matrix[j][i] = tmp
                tmp += 1
        return matrix
