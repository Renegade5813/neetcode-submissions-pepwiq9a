from collections import defaultdict
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        count_row = [0] * len(picture)
        count_col = [0] * len(picture[0])
        ans = 0
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    count_row[i] += 1
                    count_col[j] += 1
        
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B' and count_row[i] == 1 and count_col[j] == 1:
                    ans += 1
        return ans