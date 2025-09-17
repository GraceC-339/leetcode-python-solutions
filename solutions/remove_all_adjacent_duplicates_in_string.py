class Solution:
    def removeDuplicates(self, s: str) -> str:
        # use stack - LIFO

        stack = [] #to store the chars

        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)