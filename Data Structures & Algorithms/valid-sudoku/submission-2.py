class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck = set()
        colCheck = set()
        boxCheck = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                b = (i // 3) * 3 + (j // 3)
                if (i, val) in rowCheck or (j, val) in colCheck or (b, val) in boxCheck:
                    return False
                rowCheck.add((i, val))
                colCheck.add((j, val))
                boxCheck.add((b, val))
        return True