import collections
from typing import List


class Solution:
    def pacific_atlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []

        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            q = collections.deque(starts)

            while q:
                r, c = q.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        if heights[nr][nc] >= heights[r][c]:
                            visited.add((nr, nc))
                            q.append((nr, nc))
            return visited

        pacific_starts = []
        atlantic_starts = []

        for r in range(rows):
            pacific_starts.append((r, 0))
            atlantic_starts.append((r, cols - 1))

        for c in range(cols):
            pacific_starts.append((0, c))
            atlantic_starts.append((rows - 1, c))

        pacific_visited = bfs(pacific_starts)
        atlantic_visited = bfs(atlantic_starts)

        return list(pacific_visited & atlantic_visited)