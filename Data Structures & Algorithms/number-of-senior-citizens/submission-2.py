class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            if int(i[11] + i[12]) > 60:
                count += 1

        return count