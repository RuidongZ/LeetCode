# -*- Encoding:UTF-8 -*-

# 498. Diagonal Traverse

# Given a matrix of M x N elements (M rows, N columns),
# return all elements of the matrix in diagonal order as shown in the below image.

# Example:
# Input:
# [
#     [ 1, 2, 3 ],
#     [ 4, 5, 6 ],
#     [ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]

# Note:
# The total number of elements of the given matrix will not exceed 10,000.


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        if not matrix:
            return ans
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = 0
        d = 1
        num = row * col
        cnt = 0
        while cnt < num:
            ans.append(matrix[i][j])
            cnt += 1
            if d > 0:
                if i > 0 and j < col-1:
                    i -= 1
                    j += 1
                elif i == 0 and j < col-1:
                    j += 1
                    d = -d
                elif j == col-1:
                    i += 1
                    d = -d
            else:
                if j > 0 and i < row-1:
                    i += 1
                    j -= 1
                elif j == 0 and i < row-1:
                    i += 1
                    d = -d
                elif i == row-1:
                    j += 1
                    d = -d
        return ans
