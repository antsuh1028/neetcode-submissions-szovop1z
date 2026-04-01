class Solution:
    def calculate(self, s: str) -> int:
        prev = "+"
        num = 0
        stack = []

        for i,ch in enumerate(s):
            print(ch)
            print(prev)
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (not ch.isdigit() and ch != " ") or i == len(s) - 1:
                print(prev, ch)
                if prev == "+":
                    print("here")
                    stack.append(num)
                elif prev == "-":
                    stack.append(-num)
                elif prev == "*":
                    stack.append(stack.pop() * num)
                elif prev == "/":
                    temp = stack.pop()
                    if temp  < 0:
                        stack.append(-( -temp // num))
                    else:
                        stack.append(temp // num)
                num = 0
                prev = ch
                print(stack)
        return sum(stack)

        opps = "+-/*"
        num = "1234567890"
        #[3,2]
        for op in s:
            if op in opps:
                if prev == "-":
                    stack.append(-stack.pop())
                elif prev == "*":
                    temp = stack.pop()
                    stack.append(stack.pop() * temp)
                elif prev == "/":
                    temp = stack.pop()
                    stack.append(stack.pop() // temp)
                prev = op
                stack.append(0)
            else:
                if op in num:
                    stack[-1] *= 10
                    stack[-1] += int(op)
                    print(stack)
        if prev == "-":
            stack.append(-stack.pop())
        elif prev == "*":
            stack.append(stack.pop() * stack.pop())
        elif prev == "/":
            temp = stack.pop()
            stack.append(stack.pop() // temp)
        
        return sum(stack)
        
        