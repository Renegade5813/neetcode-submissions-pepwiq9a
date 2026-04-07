class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch in pair.values():  # opening brackets
                stack.append(ch)
            elif ch in pair:  # closing brackets
                if not stack or stack[-1] != pair[ch]:
                    return False
                stack.pop()
            else:
                # If there are any other characters (not in the allowed set)
                return False

        return not stack