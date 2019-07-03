'''
Quest:

    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
    A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

    Example:
    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    Note:
    Although the above answer is in lexicographical order, your answer could be in any order you want.

Solution:

'''

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return [] # seems like if not input, output should be [] instead of [""]

        res = [""]  # "" is important, or there wouldn't be any return
        mapdict = {"2": "abc",
                   "3": "def",
                   "4": "ghi",
                   "5": "jkl",
                   "6": "mno",
                   "7": "pqrs",
                   "8": "tuv",
                   "9": "wxyz"
                   }
        tmp = []
        for i in digits:
            for j in mapdict[i]:
                for k in res:
                    tmp.append(k + j)
            res = tmp
            tmp = []

        return res

test = Solution()
x = "23"
print(test.letterCombinations(x))