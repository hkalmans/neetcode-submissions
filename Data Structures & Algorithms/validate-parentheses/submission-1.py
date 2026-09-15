class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cl = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in cl:
                if stack and stack[-1] == cl[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False