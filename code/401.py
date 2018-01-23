# -*- Encoding:UTF-8 -*-

# 401. Binary Watch

# A binary watch has 4 LEDs on the top which represent the hours (0-11),
# and the 6 LEDs on the bottom represent the minutes (0-59).
#
# Each LED represents a zero or one, with the least significant bit on the right.
#
# For example, the above binary watch reads "3:25".
#
# Given a non-negative integer n which represents the number of LEDs that are currently on,
# return all possible times the watch could represent.
#
# Example:
#
# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
# Note:
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid,
# it should be "10:02".


class Solution(object):
    def __init__(self):
        self.ans = []

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        nums = [0] * 10
        self.dfs(nums, 0, num)
        return self.ans

    def dfs(self, nums, index, num):
        if num == 0:
            tmp = self.idValid(nums)
            if tmp:
                self.ans.append(tmp)
            return
        for i in range(index, len(nums)-num+1):
            nums[i] = 1
            self.dfs(nums, i+1, num-1)
            nums[i] = 0

    def idValid(self, nums):
        a = nums[:4]
        b = nums[4:]
        h = 0
        m = 0
        for i, c in enumerate(a):
            h += c * (2**i)
        if h > 11:
            return None
        for i, c in enumerate(b):
            m += c * (2**i)
        if m > 59:
            return None
        return "{}:{:02d}".format(h, m)
