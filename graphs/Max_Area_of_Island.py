from typing import List, Set


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        counter: List[int] = [0,0]

        def dfs(row, col):
            # 1. Bounds check
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            # 2. Check if water OR already visited
            if grid[row][col] == 0:
                return

            # 3. Mark as visited (Modify the grid directly)
            grid[row][col] = 0
            counter[0] += 1

            # 4. Visit neighbors
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for r in range(rows):
            for c in range(cols):
                # If we find a piece of land '1', it's a NEW island
                if grid[r][c] == 1:
                    dfs(r, c)
                    counter[1] = max(counter[1], counter[0])
                    counter[0] = 0

        return counter[1]

grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

sol = Solution()
sol.maxAreaOfIsland(grid)

