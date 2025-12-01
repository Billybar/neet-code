from typing import List, Set


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate mat

        # if cell == 1
        # dfs() until
        # mark visited
        # islands += 1

        # return islands

        rows, cols = len(grid), len(grid[0])
        visited: Set[tuple[int,int]] = set()
        islands = 0

        def dfs(row,col):
            # avoid indexError
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if grid[row][col] == '1' and (row,col) not in visited:
                visited.add((row,col)) # each pos is unique

            # go to all directions
            dfs(row+1, col)     # down
            dfs(row-1, col)     # up
            dfs(row, col-1)     # left
            dfs(row, col+1)     # right

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    # explore island by backtracking
                    # no need to know - only to mark as visited
                    dfs(r,c)
                    islands += 1

        return islands


grid: List[List[str]] = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]

sol = Solution()
sol.numIslands(grid)

