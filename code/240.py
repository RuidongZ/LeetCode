# -*- Encoding:UTF-8 -*-

# 240. Search a 2D Matrix II

# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# For example,
#
# Consider the following matrix:
#
# [
#     [1,   4,  7, 11, 15],
#     [2,   5,  8, 12, 19],
#     [3,   6,  9, 16, 22],
#     [10, 13, 14, 17, 24],
#     [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
#
# Given target = 20, return false.


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row = 0
        while row < len(matrix):
            if matrix[row][0] > target:
                return False

            if matrix[row][-1] < target:
                row += 1
                continue

            for n in matrix[row]:
                if n > target:
                    break
                if n == target:
                    return True
            row += 1
        return False
