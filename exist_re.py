'''
Quest:
    Given a 2D board and a word, find if the word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cell,
    where "adjacent" cells are those horizontally or vertically neighboring.
    The same letter cell may not be used more than once.

    Example:
    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    Given word = "ABCCED", return true.
    Given word = "SEE", return true.
    Given word = "ABCB", return false.

Solution:
    - dfs, use "#" to cover all the visited char
    - but why do we need to use "tmp" for storing the current board[i][j]?
        what's the dif between var and self.var

'''

class Solution:
    def exist(self, board, word):
        if not board:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True

        return False

    def dfs(self, board, i, j, word):
        # finally find the path
        if len(word) == 0:
            return True
        # out of range or doesn't match
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        print("find", board[i][j])
        board[i][j] = "#"
        res = self.dfs(board, i + 1, j, word[1:]) or \
              self.dfs(board, i - 1, j, word[1:]) or \
              self.dfs(board, i, j + 1, word[1:]) or \
              self.dfs(board, i, j - 1, word[1:])
        board[i][j] = word[0]
        return res

test = Solution()
board = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
print(test.exist(board, "CFS"))