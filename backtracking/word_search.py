from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len, col_len = len(board), len(board[0])
        visited = set()

        def dfs(pos, i, j):
            # 1. Success Case
            if pos == len(word):
                return True

            # 2. Boundary Checks (Added i < 0 and j < 0)
            if (i < 0 or i >= row_len or
                    j < 0 or j >= col_len or
                    pos >= len(word)):
                return False

            # 3. Visited or Mismatch Check
            if (i, j) in visited or board[i][j] != word[pos]:
                return False

            # 4. Mark Visited
            visited.add((i, j))

            # 5. Recursive Step
            res = (dfs(pos + 1, i + 1, j) or  # down
                   dfs(pos + 1, i - 1, j) or  # up
                   dfs(pos + 1, i, j - 1) or  # left
                   dfs(pos + 1, i, j + 1))  # right

            # 6. CRITICAL: Backtrack (Unmark visited)
            visited.remove((i, j))

            return res

        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] == word[0]:  # Optimization: only start if first letter matches
                    if dfs(0, i, j):
                        return True
        return False

board=[["A","B","C","D"],["S","A","A","T"],["A","C","A","E"]]
word = "CAT"
sol = Solution()
sol.exist(board,word)

