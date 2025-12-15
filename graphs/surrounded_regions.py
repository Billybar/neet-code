from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        # Recursive DFS function
        # Purpose: Mark all 'O's connected to the current 'O' with a temporary sign
        def dfs(r, c):
            # Base case: Out of bounds or cell is not 'O'
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return

            # Mark the current cell as "safe" (e.g., 'T' for Temp/Safe)
            board[r][c] = 'T'

            # Continue traversing in 4 directions (no diagonals)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Iterate over the board's border (boundary)
        # If an 'O' is found on the border, run DFS from it
        for r in range(rows):
            for c in range(cols):
                # Check if we are on the border (first/last row or first/last column)
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    if board[r][c] == 'O':
                        dfs(r, c)

        # Step 2: Iterate over the entire board to perform the final flip
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    # This is an 'O' that wasn't reached from the border -> It is surrounded! Change to 'X'
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    # This was an 'O' connected to the border -> Restore it to original 'O'
                    board[r][c] = 'O'