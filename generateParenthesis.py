'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        left, right = n, n
        self.res = []
        self.dfs(left, right, "")
        return self.res

    def dfs(self, left, right, string):
        if left > right:
            return
        if not left and not right:
            self.res.append(string)
            return
        if left:
            self.dfs(left - 1, right, string + "(")
        if right:
            self.dfs(left, right - 1, string + ")")

test = Solution()
print(test.generateParenthesis(3))