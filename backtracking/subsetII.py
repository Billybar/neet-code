from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # to avoid duplicate i need to use set
        subsets = set()

        def dfs(subset,i):

            if i >= len(nums):
                subsets.add(tuple(subset)) # to avoid duplicate
                return None

            # 1. take it
            subset.append(nums[i])
            dfs(subset,i+1)

            # 2. not take it - backtracking
            subset.pop()
            dfs(subset, i+1)
            return

        nums.sort()
        dfs([], 0)
        return list(subsets)
