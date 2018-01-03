# -*- Encoding:UTF-8 -*-

# 696. Count Binary Substrings

# Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's,
# and all the 0's and all the 1's in these substrings are grouped consecutively.

# Substrings that occur multiple times are counted the number of times they occur.
# Example 1:
# Input: "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's:
# "0011", "01", "1100", "10", "0011", and "01".

# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
#
# Example 2:
# Input: "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
#
# Note:
# s.length will be between 1 and 50,000.
# s will only consist of "0" or "1" characters.


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        i = 0
        while i < len(s):
            tmp = s[i]
            j = i
            while s[j] == tmp:
                j += 1
                if j == len(s):
                    return ans
            length = j - i
            k = j + 1
            while k - j < length and k < len(s):
                if s[k] == tmp:
                    break
                k += 1
            ans += k - j
            i = j
        '''
        # Time Limit Exceeded
        ans = 0
        for i in range(len(s)):
            tmp = s[i]
            j = i
            while s[j] == tmp:
                j += 1
                if j == len(s):
                    return ans
            length = j - i
            if j+length <= len(s):
                for c in s[j:j+length]:
                    if c == tmp:
                        ans -= 1
                        break
                ans += 1
        '''
sol = Solution()
ans = sol.countBinarySubstrings("00110")