import collections
from typing import List

ROTTEN = 2
FRESH = 1


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        num_of_fresh = [0]
        minute = 0

        def add_direction(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] == FRESH:
                # its become rotten - so add to q
                grid[r][c] = ROTTEN
                q.append((r, c))
                num_of_fresh[0] -=1

        # add rotten
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == ROTTEN:
                    q.append((r, c))
                if grid[r][c] == FRESH:
                    num_of_fresh[0] += 1

        # run multi bfs
        while q and num_of_fresh[0]>0:
            minute += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                add_direction(r + 1, c)
                add_direction(r - 1, c)
                add_direction(r, c + 1)
                add_direction(r, c - 1)

        if num_of_fresh[0] > 0:
            return -1
        return minute


grid = [[1,1,0],[0,1,1],[0,1,2]]
sol = Solution()
print(sol.orangesRotting(grid))