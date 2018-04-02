# -*- Encoding:UTF-8 -*-

# 670. Maximum Swap

# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
# Return the maximum valued number you could get.
#
# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
# Note:
# The given number is in the range [0, 10^8]


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        strnum = list(str(num))
        sortedstrnum = sorted(strnum, reverse=True)

        for i in range(len(strnum)):
            if strnum[i] != sortedstrnum[i]:
                tmp = strnum[i]
                strnum[i] = sortedstrnum[i]
                idx = strnum[::-1].index(sortedstrnum[i])
                strnum[len(strnum)-1-idx] = tmp
                break
        return int("".join(strnum))
