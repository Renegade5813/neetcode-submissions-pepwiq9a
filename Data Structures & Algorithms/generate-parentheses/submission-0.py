class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(op,cl, sub):
            if len(sub) ==2*n:
                res.append("".join(sub))
                return
            if op<n:
                sub.append("(")
                dfs(op+1, cl, sub)
                sub.pop()
            if cl<op:
                sub.append(")")
                dfs(op, cl+1, sub)
                sub.pop()

        dfs(0,0, [])
        return res