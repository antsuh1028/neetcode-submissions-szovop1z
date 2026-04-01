class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0 for temp in temperatures]

        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                print(i,j)
                if temperatures[j] > temperatures[i]:
                    arr[i] = j - i
                    break
        return arr
