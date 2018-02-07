# -*- Encoding:UTF-8 -*-

# 593. Valid Square

# Given the coordinates of four points in 2D space, return whether the four points could construct a square.
#
# The coordinate (x,y) of a point is represented by an integer array with two integers.
#
# Example:
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
# Note:
#
# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).
# Input points have no order.


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        l = []
        l.append(self.distance(p1, p2))
        l.append(self.distance(p1, p3))
        l.append(self.distance(p1, p4))
        l.append(self.distance(p2, p3))
        l.append(self.distance(p2, p4))
        l.append(self.distance(p3, p4))

        l = sorted(l)
        if l[3] != l[4] and l[0] == l[3] and l[4] == l[5] and l[0]*2 == l[5]:
            return True
        return False

    def distance(self, p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
