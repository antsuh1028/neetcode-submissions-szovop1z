class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0 for temp in temperatures]
        stack = [(0, temperatures[0])]

        for i in range(1,len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                
                temp = stack.pop()
                print(temp)
                print(temperatures[i])
                arr[temp[0]] =  i - temp[0]
            stack.append((i,temperatures[i]))
        return arr