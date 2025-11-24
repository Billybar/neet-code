from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            # if its leaf - end of a branch
            if i>= len(nums):
                res.append(subset.copy())
                return

            # Option 1. include num
            subset.append(nums[i])
            dfs(i+1)

            # Option 2. NOT including num
            subset.pop()
            dfs(i+1)

        # iterate the nums list
        dfs(0)
        return res