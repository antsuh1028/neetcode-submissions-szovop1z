class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+": lambda x, y: x+y, "-": lambda x, y: x-y,
         "*": lambda x, y: x*y, "/": lambda x, y: int(x/y)}

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                b, a = stack.pop(), stack.pop()
                res = operations[token](a,b)
                stack.append(res)
        return stack[0]
