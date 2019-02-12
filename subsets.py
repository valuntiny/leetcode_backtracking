'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        self.res = []
        self.dfs(nums, [], 0)
        return self.res

    def dfs(self, nums, sub, i):
        if i == len(nums):
            self.res.append(sub)
            return
        self.dfs(nums, sub, i + 1)
        self.dfs(nums, sub + [nums[i]], i + 1)

test = Solution()
print(test.subsets([1,2,3]))