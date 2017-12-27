# -*- Encoding:UTF-8 -*-

# 419. Battleships in a Board
# Given an 2D board, count how many battleships are in it.
# The battleships are represented with 'X's, empty slots are represented with '.'s.
# You may assume the following rules:
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically.
# In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column),
# where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

# Follow up:
# Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        cnt = 0
        for i, x in enumerate(board):
            for j, y in enumerate(x):
                if y == "X":
                    if i-1 >= 0 and board[i-1][j] == "X":
                        continue
                    if j-1 >= 0 and board[i][j-1] == "X":
                        continue
                    cnt += 1
        return cnt
