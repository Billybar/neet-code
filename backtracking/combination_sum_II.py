from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # decision tree
        res = set()
        candidates.sort()

        def dfs(total: int, i: int, subset: List[int]):

            if total == target:
                res.add(tuple(subset))
                return None

            if total > target or i >= len(candidates):
                return None

            # Decision 1: Include candidates[i]
            subset.append(candidates[i])
            dfs(total + candidates[i], i + 1, subset)  # Stay at i

            # BACKTRACK: Remove the number we just added so we can try the "Exclude" path
            subset.pop()

            # Decision 2: Exclude nums[i]
            dfs(total, i + 1, subset)  # Move to i + 1
            return None

        dfs(0, 0, [])
        return [list(combination) for combination in res]

sol = Solution()
nums1 = [2,5,6,9]
target1 = 9

print(sol.combinationSum(nums1,target1))





