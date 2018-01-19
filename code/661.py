# -*- Encoding:UTF-8 -*-

# 661. Image Smoother

# Given a 2D integer matrix M representing the gray scale of an image,
# you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down)
# of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

# Example 1:
# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# Note:
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = [([0]*len(M[0])) for _ in range(len(M)) ]
        for i in range(len(M)):
            for j in range(len(M[0])):
                ans[i][j] = self.smooth(M, i, j)
        return ans

    def smooth(self, M, i, j):
        cnt = M[i][j]
        sum = 1
        r = len(M)
        c = len(M[0])
        if i-1 >= 0 and j-1 >= 0:
            cnt += M[i-1][j-1]
            sum += 1
        if i-1 >= 0:
            cnt += M[i-1][j]
            sum += 1
        if i-1 >= 0 and j+1 <= c-1:
            cnt += M[i-1][j+1]
            sum += 1
        if j+1 <= c-1:
            cnt += M[i][j+1]
            sum += 1
        if i+1 <= r-1 and j+1 <= c-1:
            cnt += M[i+1][j+1]
            sum += 1
        if i+1 <= r-1:
            cnt += M[i+1][j]
            sum += 1
        if i+1 <= r-1 and j-1 >= 0:
            cnt += M[i+1][j-1]
            sum += 1
        if j-1 >= 0:
            cnt += M[i][j-1]
            sum += 1
        return cnt // sum
