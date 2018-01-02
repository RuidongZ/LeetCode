# -*- Encoding:UTF-8 -*-

# 526. Beautiful Arrangement

# Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array
# that is constructed by these N numbers successfully if one of the following is true
# for the ith position (1 <= i <= N) in this array:
# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.

# Now given N, how many beautiful arrangements can you construct?
#
# Example 1:
# Input: 2
# Output: 2
# Explanation:
#
# The first beautiful arrangement is [1, 2]:
#
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
#
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
#
# The second beautiful arrangement is [2, 1]:
#
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
#
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
# Note:
# N is a positive integer and will not exceed 15.


class Solution(object):
    cnt = 0
    visited = None
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.visited = [0] * N
        self.DFS(N)
        return self.cnt

    def DFS(self, idx):
        if idx == 0:
            self.cnt += 1
            return
        for i in range(len(self.visited)):
            if self.visited[i] != 1:
                if idx % (i+1) == 0 or (i+1) % idx == 0:
                    self.visited[i] = 1
                    self.DFS(idx-1)
                    self.visited[i] = 0
        ''' 
        # Time Limit Exceeded
        visited = [0] * N
        ans = self.DFS(visited, 1)
        return ans

    def DFS(self, visited, idx):
        if idx == len(visited)+1:
            return 1
        total = 0
        for i, j in enumerate(visited):
            if j != 1:
                if (i+1) % idx == 0 or idx % (i+1) == 0:
                    import copy
                    newVisited = copy.copy(visited)
                    newVisited[i] = 1
                    total += self.DFS(newVisited, idx+1)
        return total
        '''
