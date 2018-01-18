# -*- Encoding:UTF-8 -*-

# 539. Minimum Time Difference

# Given a list of 24-hour clock time points in "Hour:Minutes" format,
# find the minimum minutes difference between any two time points in the list.
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# Note:
# The number of time points in the given list is at least 2 and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timePoints = sorted(timePoints)
        time = []
        for i in timePoints:
            t = i.split(":")
            h = int(t[0])
            m = int(t[1])
            time.append(h*60+m)
        time.append(time[0]+1440)

        ans = time[1] - time[0]
        for i in range(1, len(time)-1):
            if time[i+1] - time[i] < ans:
                ans = time[i+1]-time[i]
        return ans
