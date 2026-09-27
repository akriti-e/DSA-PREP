class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                print(stack)
                # Extract characters until '('
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()  # remove '('
                stack.extend(temp)  # push reversed back
            else:
                stack.append(char)
        return "".join(stack)
