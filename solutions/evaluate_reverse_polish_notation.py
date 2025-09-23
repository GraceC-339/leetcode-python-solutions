class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = ('+', '-', '*', '/')

        for char in tokens:
            if char in operators:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if char == '+':
                    temp = num1 + num2
                    stack.append(temp)
                elif char == '-':
                    temp = num2 - num1
                    stack.append(temp)
                elif char == '*':
                    temp = num1 * num2
                    stack.append(temp)
                elif char == '/':
                    temp = num2 / num1
                    stack.append(int(temp))
            else:
                stack.append(int(char))
        
        return stack[0]
