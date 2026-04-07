class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record: List[int] = []
        for i,x in enumerate(operations):
            if x == '+':
                val = record[-1]+record[-2]
                record.append(val)
            elif x == 'D':
                val = 2*record[-1]
                record.append(val)
            elif x == 'C':
                record.pop()
            else:
                record.append(int(x))
        
        score = 0
        for i in record:
            score += i
        
        return score
