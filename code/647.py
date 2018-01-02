# -*- Encoding:UTF-8 -*-

# 647. Palindromic Substrings

# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
#
# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# Note:
# The input string length won't exceed 1000.


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1

        start = 0
        ansIndex = []
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                n = i - start + 1

                j = 1
                while start-j >= 0 and i+j <= len(s)-1:
                    if s[start-j] == s[i+j]:
                        j += 1
                    else:
                        break
                num = n*(n+1)//2 + j-1
                ansIndex.append(num)
                start = i+1

        n = len(s) - start
        num = n*(n+1)//2
        ansIndex.append(num)

        return sum(ansIndex)
