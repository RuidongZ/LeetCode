# -*- Encoding:UTF-8 -*-

# 394. Decode String

# Given an encoded string, return it's decoded string.
#
# The encoding rule is: k[encoded_string],
# where the encoded_string inside the square brackets is being repeated exactly k times.
# Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits
# and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        numstack = []
        charstack = []
        curchar = ""
        ans = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                while s[j].isdigit():
                    j += 1
                numstack.append(int(s[i:j]))
                i = j
            elif s[i] == '[':
                j = i + 1
                while s[j].isalpha():
                    j += 1
                charstack.append(s[i+1:j])
                i = j
            elif s[i] == ']':
                tmp = charstack.pop()
                times = numstack.pop()
                if charstack:
                    charstack[-1] += tmp*times
                else:
                    ans += tmp * times
                i += 1
            else:
                if charstack:
                    charstack[-1] += s[i]
                else:
                    ans += s[i]
                i += 1
        return ans
