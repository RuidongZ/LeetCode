# -*- Encoding:UTF-8 -*-

# 657. Judge Route Circle
# Initially, there is a Robot at position (0, 0).
# Given a sequence of its moves, judge if this robot makes a circle,
# which means it moves back to the original place.
#
# The move sequence is represented by a string. And each move is represent by a character.
# The valid robot moves are R (Right), L (Left), U (Up) and D (down).
# The output should be true or false representing whether the robot makes a circle.
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        R_count = 0
        L_count = 0
        U_count = 0
        D_count = 0
        for i in moves:
            if i == 'R':
                R_count += 1
            elif i == 'L':
                L_count += 1
            elif i == 'U':
                U_count += 1
            else:
                D_count += 1

        if R_count == L_count and U_count == D_count:
            return True
        else:
            return False
