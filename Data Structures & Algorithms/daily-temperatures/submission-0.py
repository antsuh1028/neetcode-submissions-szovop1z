class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        stack.append(0)

        for i in range(1,len(temperatures)):
            print(stack)
            print("before: ", temperatures[i], temperatures[stack[-1]])
            while stack and temperatures[i] > temperatures[stack[-1]]:
                print(temperatures[i], temperatures[stack[-1]])
                top = stack.pop()
                result[top] = i - top

            stack.append(i)
        return result
            
        