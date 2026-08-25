class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ')]}':
                if len(stack) == 0:
                    return False
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == ']' and stack[-1] == '[': 
                    stack.pop()
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False 
        if len(stack) == 0:
            return True 
        else:
            return False
