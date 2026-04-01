class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = []
        ops = {"+": lambda x,y:y+x,
        "-": lambda x,y:y-x,
        "/": lambda x,y:int(y/x),
        "*": lambda x,y:y*x,}

        for token in tokens:
            if token.strip("-").isnumeric():
                operations.append(int(token))
            else:
                x,y = operations.pop(),operations.pop()
                operations.append(ops[token](x,y))


        return int(operations.pop())