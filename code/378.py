# -*- Encoding:UTF-8 -*-

# 378. Kth Smallest Element in a Sorted Matrix

# Given a n x n matrix where each of the rows and columns are sorted in ascending order,
# find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example:
#
# matrix = [
#              [ 1,  5,  9],
#              [10, 11, 13],
#              [12, 13, 15]
#          ],
# k = 8,
#
# return 13.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n2.


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        """
        # Better way
        n = len(matrix)
        lo = matrix[0][0]
        hi = matrix[-1][-1]

        while lo <= hi:
            mid = (lo + hi)/2
            cnt = 0
            j = n-1
            for i in range(n):
                while j >= 0:
                    if matrix[i][j] > mid:
                        j -= 1
                    else:
                        cnt += j+1
                        break
            if cnt >= k:
                hi = mid-1
            else:
                lo = mid+1
            #print cnt, hi, lo, k, mid

        return hi+1
        """
        m = []
        for i in matrix:
            m.extend(i)
        return sorted(m)[k-1]
