class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": lambda x, y: x + y, 
            "-": lambda x, y: x - y,  # Fixed: was y - x
            "*": lambda x, y: x * y, 
            "/": lambda x, y: int(x / y)  # Fixed: handle negative division correctly
        }

        for token in tokens:
            if token not in operations:
                stack.append(int(token))  # Fixed: convert to int when pushing
            else:
                b = stack.pop()  # Second operand
                a = stack.pop()  # First operand
                res = operations[token](a, b)  # Fixed: correct order
                stack.append(res)
        
        return stack[0]