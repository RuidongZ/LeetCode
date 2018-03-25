# -*- Encoding:UTF-8 -*-

# 686. Repeated String Match

# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it.
# If no such solution, return -1.
#
# For example, with A = "abcd" and B = "cdabcdab".
#
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it;
# and B is not a substring of A repeated two times ("abcdabcd").
#
# Note:
# The length of A and B will be between 1 and 10000.


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        times = int(len(B)/len(A))
        if len(set(A)) < len(set(B)):
            return -1
        if B in A*times:
            return times
        elif B in A*(times+1):
            return times+1
        elif B in A*(times+2):
            return times+2
        else:
            return -1


