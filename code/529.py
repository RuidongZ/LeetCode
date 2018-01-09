# -*- Encoding:UTF-8 -*-

# 529. Minesweeper

# Let's play the minesweeper game (Wikipedia, online game)!

# You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine,
# 'E' represents an unrevealed empty square,
# 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines,
# digit ('1' to '8') represents how many mines are adjacent to this revealed square,
# and finally 'X' represents a revealed mine.
#
# Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'),
# return the board after revealing this position according to the following rules:
#
# If a mine ('M') is revealed, then the game is over - change it to 'X'.
# If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B')
# and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8')
# representing the number of adjacent mines.
# Return the board when no more squares will be revealed.

# Example 1:
# Input:
# [['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]
# Click : [3,0]
#
# Output:
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Explanation:
#
# Example 2:
# Input:
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
# Click : [1,2]

# Output:
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'X', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Explanation:
#
# Note:
# The range of the input matrix's height and width is [1,50].
# The click position will only be an unrevealed square ('M' or 'E'),
# which also means the input board contains at least one clickable square.
# The input board won't be a stage when game is over (some mines have been revealed).
# For simplicity, not mentioned rules should be ignored in this problem.
# For example, you don't need to reveal all the unrevealed mines when the game is over,
# consider any cases that you will win the game or flag any squares.


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
        else:
            self.dfs(board, click)
        return board

    def dfs(self, board, idx):
        i, j = idx[0], idx[1]
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if board[i][j] == "E":
            num = self.checkAroud(board, idx)
            if num == 0:
                board[i][j] = "B"
                self.dfs(board, [i-1, j-1])
                self.dfs(board, [i-1, j])
                self.dfs(board, [i-1, j+1])
                self.dfs(board, [i, j+1])
                self.dfs(board, [i+1, j+1])
                self.dfs(board, [i+1, j])
                self.dfs(board, [i+1, j-1])
                self.dfs(board, [i, j-1])
            else:
                board[i][j] = str(num)

    def checkAroud(self, board, idx):
        cnt = 0
        i, j = idx[0], idx[1]
        if i-1 >= 0 and j-1 >= 0 and board[i-1][j-1] == "M":
            cnt += 1
        if i-1 >= 0 and board[i-1][j] == "M":
            cnt += 1
        if i-1 >= 0 and j+1 <= len(board[0])-1 and board[i-1][j+1] == "M":
            cnt += 1
        if j+1 <= len(board[0])-1 and board[i][j+1] == "M":
            cnt += 1
        if i+1 <= len(board)-1 and j+1 <= len(board[0])-1 and board[i+1][j+1] == "M":
            cnt += 1
        if i+1 <= len(board)-1 and board[i+1][j] == "M":
            cnt += 1
        if i+1 <= len(board)-1 and j-1 >= 0 and board[i+1][j-1] == "M":
            cnt += 1
        if j-1 >= 0 and board[i][j-1] == "M":
            cnt += 1
        return cnt
