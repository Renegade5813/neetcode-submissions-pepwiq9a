class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        boxes = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                b = (r // 3) * 3 + (c // 3)

                if (r, val) in rows or (c, val) in cols or (b, val) in boxes:
                    return False

                rows.add((r, val))
                cols.add((c, val))
                boxes.add((b, val))

        return True