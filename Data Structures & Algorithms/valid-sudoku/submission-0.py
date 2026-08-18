class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [set() for _ in range(9)]
        row = [set() for _ in range(9)]
        sq = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                box_idx = (r // 3) * 3 + (c // 3)
                if (board[r][c] in col[c]
                    or board[r][c] in row[r]
                    or board[r][c] in sq[box_idx]):
                    return False
                col[c].add(board[r][c])
                row[r].add(board[r][c])
                sq[box_idx].add(board[r][c])
        return True
        