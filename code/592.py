# -*- Encoding:UTF-8 -*-

# 592. Fraction Addition and Subtraction

# Given a string representing an expression of fraction addition and subtraction,
# you need to return the calculation result in string format. The final result should be irreducible fraction.
# If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1.
# So in this case, 2 should be converted to 2/1.

# Example 1:
# Input:"-1/2+1/2"
# Output: "0/1"
# Example 2:
# Input:"-1/2+1/2+1/3"
# Output: "1/3"
# Example 3:
# Input:"1/3-1/2"
# Output: "-1/6"
# Example 4:
# Input:"5/3+1/3"
# Output: "2/1"
# Note:
# The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
# Each fraction (input and output) has format ±numerator/denominator.
# If the first input fraction or the output is positive, then '+' will be omitted.
# The input only contains valid irreducible fractions,
# where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1,
# it means this fraction is actually an integer in a fraction format defined above.
# The number of given fractions will be in the range [1,10].
# The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.


class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        # Importance Start
        def gcm(a, b):
            if a >= b:
                if a % b == 0:
                    return b
                else:
                    return gcm(b, a - b)
            else:
                return gcm(b, a)

        def lcm(a, b):
            return a * b // gcm(a, b)
        # Importance End
        expressions = expression.split("/")
        nums = []
        for i in range(1, len(expressions)):
            if '+' in expressions[i]:
                s = expressions[i].split("+")
                nums.append([int(expressions[i-1]), int(s[0])])
                expressions[i] = int(s[1])
            elif '-' in expressions[i]:
                s = expressions[i].split("-")
                nums.append([int(expressions[i-1]), int(s[0])])
                expressions[i] = -int(s[1])
            else:
                nums.append([int(expressions[i-1]), int(expressions[i])])
        if len(nums) == 0:
            return "0/1"
        if len(nums) == 1:
            return expression
        l = lcm(nums[0][1], nums[1][1])
        for i in range(2, len(nums)):
            l = lcm(l, nums[i][1])
        sum = 0
        for i in nums:
            sum += i[0] * (l // i[1])
        if sum == 0:
            return "0/1"
        g = gcm(l, abs(sum))
        sum = str(sum // g)
        l = str(l //g)
        return sum + "/" + l
