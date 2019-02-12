'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapdict = {"2": "abc",
                   "3": "def",
                   "4": "ghi",
                   "5": "jkl",
                   "6": "mno",
                   "7": "pqrs",
                   "8": "tuv",
                   "9": "wxyz"
                   }
        res = [""]
        if len(digits) == 0:
            return []
        for i in digits:
            str = mapdict[i]
            tmp = []
            for j in str:
                for k in res:
                    tmp.append(k+j)
            res = tmp

        return res

test = Solution()
print(test.letterCombinations("234"))