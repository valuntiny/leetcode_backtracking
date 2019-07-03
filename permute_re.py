'''
Quest:
    Given a collection of distinct integers, return all possible permutations.

    Example:

    Input: [1,2,3]
    Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]

Solution:
    - dfs
'''

class Solution:
    def permute(self, nums):
        if not nums:
            return []
        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, s):
        if not nums:
            self.res.append(s)
            return
        for i in range(len(nums)):
            # couldn't use append, because append doesn't return anything
            self.dfs(nums[:i] + nums[(i+1):], s + [nums[i]])

test = Solution()
x = [1,2,3]
print(test.permute(x))