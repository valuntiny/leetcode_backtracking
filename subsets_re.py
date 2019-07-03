'''
Quest:
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

Solution:
    - still dfs? traverse each elements in nums, decide to put it in res or not
'''

class Solution:
    def subsets(self, nums):
        if not nums:
            return []

        self.res = []
        self.dfs(nums, [], 0)
        return self.res


    def dfs(self, nums, tmp, i):
        if i == len(nums):
            self.res.append(tmp)
            return
        self.dfs(nums, tmp, i + 1)
        self.dfs(nums, tmp + [nums[i]], i + 1)

test = Solution()
nums = [1,2,3]
print(test.subsets(nums))