'''
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
'''


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, perm):
        if not nums:
            self.res.append(perm)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[(i + 1):], perm + [nums[i]])

test = Solution()
print(test.permute([4,2,3]))