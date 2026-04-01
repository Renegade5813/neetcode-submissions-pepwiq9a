class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                box = (r // 3) * 3 + (c // 3)

                if (r, val) in seen or (('c', c, val)) in seen or (('b', box, val)) in seen:
                    return False

                seen.add((r, val))
                seen.add(('c', c, val))
                seen.add(('b', box, val))

        return True