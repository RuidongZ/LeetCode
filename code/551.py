# -*- Encoding:UTF-8 -*-

# 551. Student Attendance Record I

# You are given a string representing an attendance record for a student.
# The record only contains the following three characters:
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more
# than two continuous 'L' (late).
#
# You need to return whether the student could be rewarded according to his attendance record.
#
# Example 1:
# Input: "PPALLP"
# Output: True
# Example 2:
# Input: "PPALLL"
# Output: False

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Pythonic way
        # return (s.count('A') <= 1) and ('LLL' not in s)
        cntA = 0
        for idx, i in enumerate(s):
            if i == 'A':
                cntA += 1
                if cntA == 2:
                    return False
            elif i == 'L' and len(s) - idx >= 3:
                if s[idx+1] == 'L' and s[idx+2] == 'L':
                    return False
        return True
