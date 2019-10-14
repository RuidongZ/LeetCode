# -*- Encoding:UTF-8 -*-

# 17. Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.
#
# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
#
# Although the above answer is in lexicographical order, your answer could be in any order you want.
from typing import List
import itertools


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2": ['a', 'b', 'c'],
             "3": ['d', 'e', 'f'],
             "4": ['g', 'h', 'i'],
             "5": ['j', 'k', 'l'],
             "6": ['m', 'n', 'o'],
             "7": ['p', 'q', 'r', 's'],
             "8": ['t', 'u', 'v'],
             "9": ['w', 'x', 'y', 'z']}
        ans = []
        if len(digits) == 0:
            return ans
        elif len(digits) == 1:
            return d[digits]
        else:
            ans = d[digits[0]]
            for i in range(1, len(digits)):
                ans = ["".join(x) for x in itertools.product(ans, d[digits[i]])]
            return ans