from collections import defaultdict
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        col_count = defaultdict(int)
        row_single = []

        for i in range(len(picture)):
            b_count = 0
            col = -1
            for j in range(len(picture[i])):
                if picture[i][j] == 'B':
                    col_count[j] += 1
                    b_count += 1
                    col = j
            if b_count == 1:
                row_single.append(col)

        return sum(1 for col in row_single if col_count[col] == 1)

                    