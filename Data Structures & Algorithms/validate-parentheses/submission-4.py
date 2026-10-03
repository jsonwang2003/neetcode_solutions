class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{' : '}', '[' : ']'}
        stack = []

        for c in s:
            if c in ")]}":
                if not stack or c != brackets[stack.pop()]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0