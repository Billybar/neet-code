from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # get firs word position
        row_len, col_len = len(board), len(board[0])
        def dfs(letters, i,j):
            if i >= len(board) or j >= len(board[0]):
                return None

            if word.startswith(tuple(letters)):
                return None

            if letters == word:
                return True

            if i+1 < row_len:
                letters.append(board[i+1][j])
                dfs(letters, i+1,j)     # down
            if i-1 >= 0:
                letters.pop()
                letters.append(board[i-1][j])
                dfs(letters, i-1, j)    # up

            if j-1 >= 0:
                letters.pop()
                letters.append(board[i][j-1])
                dfs(letters, i, j-1)    # left

            if j+1 <= col_len:
                letters.pop()
                letters.append(board[i][j+1])
                dfs(letters, i, j+1)

        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] == word[0]:
                    if dfs([board[i][j]],i,j):
                        return True
        return False

board=[["A","B","C","D"],["S","A","A","T"],["A","C","A","E"]]
word = "CAT"
sol = Solution()
sol.exist(board,word)

