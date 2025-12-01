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

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    # explore island by backtracking
                    dfs()



