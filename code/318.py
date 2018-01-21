# -*- Encoding:UTF-8 -*-

# 318. Maximum Product of Word Lengths

# Given a string array words, find the maximum value of length(word[i]) * length(word[j])
# where the two words do not share common letters. You may assume that each word will contain only lower case letters.
# If no such two words exist, return 0.

# Example 1:
# Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# Return 16
# The two words can be "abcw", "xtfn".
#
# Example 2:
# Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# Return 4
# The two words can be "ab", "cd".
#
# Example 3:
# Given ["a", "aa", "aaa", "aaaa"]
# Return 0
# No such pair of words.


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mask = []
        n = 0
        ans = 0
        for word in words:
            tmp = 0
            for i in word:
                tmp |= 1 << (ord(i) - ord('a'))
            mask.append(tmp)
            j = 0
            while j < n:
                if mask[n] & mask[j] == 0:
                    tmp_max = len(words[n]) * len(words[j])
                    if tmp_max > ans:
                        ans = tmp_max
                j += 1
            n += 1
        return ans
