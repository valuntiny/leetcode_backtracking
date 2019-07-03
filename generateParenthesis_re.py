'''
Quest:
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    For example, given n = 3, a solution set is:

    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]

Solution:

'''

class Solution:
    def generateParenthesis(self, n):
        if n < 1:
            return []

        self.res = []
        self.dfs(n, n, "")
        return self.res


    def dfs(self, open, close, s):
        if close >= open >= 0:
            if close == 0:
                self.res.append(s)
            else:
                if open:
                    self.dfs(open - 1, close, s + "(")
                if close:
                    self.dfs(open, close - 1, s + ")")

test = Solution()
n = 3
print(test.generateParenthesis(n))