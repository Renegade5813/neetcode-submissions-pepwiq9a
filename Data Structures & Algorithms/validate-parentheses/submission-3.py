class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open_br=['(','{','[']
        clos_br=[')','}',']']
        for c in s:
            if c in (open_br):
                stack.append(c)
            else:
                index= clos_br.index(c)
                if len(stack)!=0 and stack[-1]==open_br[index]:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False

        