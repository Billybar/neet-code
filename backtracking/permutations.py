import math
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(permute: List[int], remaining_nums: List[int]):
            # base condition
            if not remaining_nums:
                res.append(permute.copy())
                return None

            # Iterate over the numbers still available to be added
            for i in range(len(remaining_nums)):

                num = remaining_nums[i]     # current num
                permute.append(num)         # add
                new_remaining = remaining_nums[:i] + remaining_nums[i + 1:]     # remove chosen numer to avoid duplicate

                # Recurse: Move to the next level of the search
                dfs(permute, new_remaining)

                # Backtrack (Remove): Undo the 'Action' by removing the number
                permute.pop()

        dfs([], nums)
        return res

sol = Solution()
sol.permute([1,2,3])