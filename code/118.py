# -*- Encoding:UTF-8 -*-

# 118. Pascal's Triangle

# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#     [1],
#     [1,1],
#     [1,2,1],
#     [1,3,3,1],
#     [1,4,6,4,1]
# ]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1],
               [1, 1]]
        if numRows <= 2:
            return ans[:numRows]

        for i in range(2, numRows):
            tmp = [1]
            for j in range(i-1):
                tmp.append(ans[i-1][j]+ans[i-1][j+1])
            tmp.append(1)
            ans.append(tmp)
        return ans
