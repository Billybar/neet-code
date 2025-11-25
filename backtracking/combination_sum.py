from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # decision tree
        res = []

        def dfs(total:int, i:int, subset:List[int]):

            if total == target:
                res.append(subset.copy())
                return None

            if total > target  or i >= len(nums):
                return None

            # Decision 1: Include nums[i]
            subset.append(nums[i])
            dfs(total + nums[i], i, subset)  # Stay at i

            # BACKTRACK: Remove the number we just added so we can try the "Exclude" path
            subset.pop()

            # Decision 2: Exclude nums[i]
            dfs(total, i + 1, subset)  # Move to i + 1
            return None

        dfs(0, 0, [])
        return res

sol = Solution()
nums1 = [2,5,6,9]
target1 = 9

print(sol.combinationSum(nums1,target1))





