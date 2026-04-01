class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            if i[11] > '6' or (i[11] == '6' and i[12] > '0'):
                count += 1

        return count