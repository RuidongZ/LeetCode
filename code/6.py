# -*- Encoding:UTF-8 -*-

# 6. ZigZag Conversion

#  The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
#  (you may want to display this pattern in a fixed font for better legibility)
#
#  P   A   H   N
#  A P L S I I G
#  Y   I   R
#  And then read line by line: "PAHNAPLSIIGYIR"
#
#  Write the code that will take a string and make this conversion given a number of rows:
#
#  string convert(string s, int numRows);
#  Example 1:
#
#  Input: s = "PAYPALISHIRING", numRows = 3
#  Output: "PAHNAPLSIIGYIR"
#  Example 2:
#
#  Input: s = "PAYPALISHIRING", numRows = 4
#  Output: "PINALSIGYAHRPI"
#  Explanation:
#
#  P     I    N
#  A   L S  I G
#  Y A   H R
#  P     I

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        interval = (numRows-1)*2

        length = len(s)
        # PAHNAPLSIIGYIR
        ans = ""
        i = 0
        while i < numRows:
            j = i
            val = interval - 2*i
            if val == 0:
                val = interval - val
            while j < length:
                ans += s[j]
                j += val
                val = interval - val
                if val == 0:
                    val = interval - val
            i += 1
        return ans
