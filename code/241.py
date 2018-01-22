# -*- Encoding:UTF-8 -*-

# 241. Different Ways to Add Parentheses

# Given a string of numbers and operators,
# return all possible results from computing all the different possible ways to group numbers and operators.
# The valid operators are +, - and *.
#
#
# Example 1
# Input: "2-1-1".
#
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Output: [0, 2]
#
#
# Example 2
# Input: "2*3-4*5"
#
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Output: [-34, -14, -10, -10, 10]


class Solution(object):
    global hm
    hm = {}
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input in hm:
            return hm[input]
        ans = []
        for i, s in enumerate(input):
            if s == '+' or s == '-' or s == '*':
                for l in self.diffWaysToCompute(input[:i]):
                    l = int(l)
                    for r in self.diffWaysToCompute(input[i+1:]):
                        r = int(r)
                        if s == '+':
                            ans.append(l+r)
                        elif s == '-':
                            ans.append(l-r)
                        else:
                            ans.append(l*r)
        if len(ans) == 0:
            ans.append(int(input))
        hm[input] = ans
        return ans
